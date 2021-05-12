-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "brewery" (
    "brewery_id" int   NOT NULL,
    "brewery_name" varchar   NOT NULL,
    CONSTRAINT "pk_brewery" PRIMARY KEY (
        "brewery_id"
     )
);

CREATE TABLE "reviewers" (
    "reviewer_id" int   NOT NULL,
    "review_profilename" varchar   NOT NULL,
    CONSTRAINT "pk_reviewers" PRIMARY KEY (
        "reviewer_id"
     )
);

CREATE TABLE "review" (
    "review_id" int   NOT NULL,
    "review_profilename" varchar   NOT NULL,
    "review_overall" float   NOT NULL,
    "review_aroma" float   NOT NULL,
    "review_appearance" float   NOT NULL,
    "review_palate" float   NOT NULL,
    "review_taste" float   NOT NULL,
    "beer_beerid" int   NOT NULL,
    CONSTRAINT "pk_review" PRIMARY KEY (
        "review_id"
     )
);

CREATE TABLE "beer" (
    "beer_beerid" int   NOT NULL,
    "beer_name" varchar   NOT NULL,
    "beer_style" int   NOT NULL,
    "beer_abv" float   NOT NULL,
    "brewery_id" int   NOT NULL,
    CONSTRAINT "pk_beer" PRIMARY KEY (
        "beer_beerid"
     )
);

CREATE TABLE "beer_style" (
    "beer_style_id" int   NOT NULL,
    "beer_style" varchar   NOT NULL,
    CONSTRAINT "pk_beer_style" PRIMARY KEY (
        "beer_style_id"
     )
);

ALTER TABLE "review" ADD CONSTRAINT "fk_review_review_profilename" FOREIGN KEY("review_profilename")
REFERENCES "reviewers" ("review_profilename");

ALTER TABLE "review" ADD CONSTRAINT "fk_review_beer_beerid" FOREIGN KEY("beer_beerid")
REFERENCES "beer" ("beer_beerid");

ALTER TABLE "beer" ADD CONSTRAINT "fk_beer_beer_style" FOREIGN KEY("beer_style")
REFERENCES "beer_style" ("beer_style_id");

ALTER TABLE "beer" ADD CONSTRAINT "fk_beer_brewery_id" FOREIGN KEY("brewery_id")
REFERENCES "brewery" ("brewery_id");

