CREATE TABLE `Users`(
  `id` VARCHAR(36) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `birth_date` DATE NOT NULL,
  `admin` BOOLEAN NOT NULL DEFAULT FALSE,
  `email` VARCHAR(100) NOT NULL,
  `password` BINARY NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_cpf` (`cpf`),
  UNIQUE KEY `user_email` (`email`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
CREATE TABLE `Topics`(
  `id` VARCHAR(36) NOT NULL,
  `topic` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `topic_topic` (`topic`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
CREATE TABLE `News`(
  `id` VARCHAR(36) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `content` TEXT NOT NULL,
  `author_id` VARCHAR(36) NOT NULL,
  `topic_id` VARCHAR(36) NOT NULL,
  `likes` INT NOT NULL DEFAULT 0,
  `created_at` DATETIME NOT NULL,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`author_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY (`topic_id`) REFERENCES `Topics`(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
CREATE TABLE `LikedNews`(
  `id` VARCHAR(36) NOT NULL,
  `user_id` VARCHAR(36) NOT NULL,
  `news_id` VARCHAR(36) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY (`news_id`) REFERENCES `News`(`id`)
) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;