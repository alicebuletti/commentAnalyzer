const axios = require('axios')
const cheerio = require('cheerio')

const show = {
    you : 'tt7335184',
    monster : 'tt13207736'
}

const totalReviews = 250;

const order = 'featured'; // time,featured

// Sorting desc: newest, asc: oldest
const sortDir = 'asc';  

async function getLatestReviews(showId) {
    try {
        const reviews = [];

        // Requête initiale pour récupérer la première page de contenu
        let paginationKey = ''; // Initialize paginationKey
        
        do {
            let url = `https://www.imdb.com/title/${showId}/reviews/_ajax?paginationKey=`;

            if(order == 'time') {
                url += `${paginationKey}&sort=submissionDate&dir=${sortDir}`;
            } else if (order == 'featured') {
                url += `${paginationKey}`;
            }
            
            const response = await axios.get(url);
            const $ = cheerio.load(response.data);
            
            // Extract the reviews from the current page
            $('.lister-item').each((index, element) => {
                const $review = $(element);
                const id = $review.data('review-id');
                const text = $review.find('.text').text().trim();
                const starRating = $review.find('.rating-other-user-rating span').text().trim()
                const datePosted = $review.find('.review-date').text().trim();
                const title = $review.find('.title').text().trim();
                
                reviews.push({
                    id,
                    title,
                    starRating,
                    datePosted,
                    text,
                });
            });

            // Extract the paginationKey for the next request
            const nextPageButton = $('.load-more-data');
            paginationKey = nextPageButton.attr('data-key');

            // IMDb recommends a delay between requests to avoid being blocked
            await new Promise(resolve => setTimeout(resolve, 2000));

        } while (reviews.length < totalReviews && paginationKey)

        return reviews

    } catch (error) {
        console.error('Error:', error.message);
        throw error;
    }
   
}

// Recuperer les reviews et les aficher sur la console
getLatestReviews(show.monster).then((reviews) => {
    console.log(JSON.stringify(reviews));
  })
  .catch((error) => {
    console.error('Failed to fetch reviews:', error.message);
  });
