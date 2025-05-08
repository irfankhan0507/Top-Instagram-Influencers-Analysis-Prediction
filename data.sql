-- 1. Create the table
CREATE TABLE instagram_influencers (
    rank INT,
    channel_info VARCHAR(255),
    influence_score FLOAT,
    posts INT,
    followers BIGINT,
    avg_likes BIGINT,
    sixty_day_eng_rate FLOAT,
    new_post_avg_like BIGINT,
    total_likes BIGINT,
    country VARCHAR(100)
);

-- 2. Insert values
INSERT INTO instagram_influencers VALUES
(1, 'cristiano', 92.00, 3300, 475800000, 8700000, 1.39, 6500000, 29000000000, 'Spain'),
(2, 'kyliejenner', 91.00, 6900, 366200000, 8300000, 1.62, 5900000, 57400000000, 'United States'),
(3, 'leomessi', 90.00, 890, 357300000, 6800000, 1.24, 4400000, 6000000000, 'Argentina'),
(4, 'therock', 89.00, 5800, 345600000, 7800000, 1.41, 5100000, 45000000000, 'United States'),
(5, 'arianagrande', 88.00, 4900, 340000000, 7200000, 1.32, 5000000, 41000000000, 'United States');

-- 3. Example Queries you can run
-- Find the influencer with the highest followers
SELECT channel_info, followers FROM instagram_influencers ORDER BY followers DESC LIMIT 1;

-- Find average influence score
SELECT AVG(influence_score) AS average_influence_score FROM instagram_influencers;

-- Top 3 countries with most influencers
SELECT country, COUNT(*) AS num_influencers FROM instagram_influencers GROUP BY country ORDER BY num_influencers DESC LIMIT 3;
