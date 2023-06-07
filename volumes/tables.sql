CREATE USER admistrador WITH SUPERUSER CREATEDB CREATEROLE PASSWORD 'tr3sv0z3sn3ws4dm1n';
CREATE TABLE "Users" (
  "id" UUID NOT NULL,
  "name" VARCHAR(100) NOT NULL,
  "cpf" VARCHAR(11) NOT NULL,
  "birth_date" DATE NOT NULL,
  "admin" BOOLEAN NOT NULL DEFAULT FALSE,
  "email" VARCHAR(100) NOT NULL,
  "password" VARCHAR(255) NOT NULL,
  "created_at" TIMESTAMP NOT NULL,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id"),
  UNIQUE ("cpf"),
  UNIQUE ("email")
);
CREATE TABLE "Topics" (
  "id" UUID NOT NULL,
  "topic" VARCHAR(100) NOT NULL,
  "created_at" TIMESTAMP NOT NULL,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id"),
  UNIQUE ("topic")
);
CREATE TABLE "News" (
  "id" UUID NOT NULL,
  "title" VARCHAR(255) NOT NULL,
  "content" TEXT NOT NULL,
  "author_id" UUID NOT NULL,
  "topic_id" UUID NOT NULL,
  "likes" INT NOT NULL DEFAULT 0,
  "created_at" TIMESTAMP NOT NULL,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id"),
  FOREIGN KEY ("author_id") REFERENCES "Users"("id"),
  FOREIGN KEY ("topic_id") REFERENCES "Topics"("id")
);
CREATE TABLE "LikedNews" (
  "id" UUID NOT NULL,
  "user_id" UUID NOT NULL,
  "news_id" UUID NOT NULL,
  "created_at" TIMESTAMP NOT NULL,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("id"),
  FOREIGN KEY ("user_id") REFERENCES "Users"("id"),
  FOREIGN KEY ("news_id") REFERENCES "News"("id")
);