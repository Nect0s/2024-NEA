/* this is and older version of the database, before it was converted to model and edited */

CREATE TABLE `accounts` (
  `a_id` integer PRIMARY KEY,
  `ac_at` timestamp,
  `email` varchar(255),
  `a_name` varchar(255),
  `gen` integer,
  `coun` integer,
  `passw` varchar(255)
);

CREATE TABLE `users` (
  `u_id` integer PRIMARY KEY,
  `username` varchar(255),
  `uc_at` timestamp
);

CREATE TABLE `messages` (
  `m_id` integer PRIMARY KEY,
  `b_id` integer,
  `u_id` integer,
  `status` integer,
  `mc_at` timestamp,
  `c_id` integer
);

CREATE TABLE `servers` (
  `se_id` integer PRIMARY KEY,
  `sc_at` timestamp,
  `s_name` varchar(255),
  `s_desc` varchar(255),
  `s_image` varchar(255),
  `owner_user_id` varchar(255)
);

CREATE TABLE `channels` (
  `c_id` integer PRIMARY KEY,
  `se_id` integer,
  `cc_at` timestamp,
  `c_name` varchar(255),
  `c_desc` varchar(255),
  `c_image` varchar(255)
);

CREATE TABLE `message_content` (
  `b_id` integer PRIMARY KEY,
  `b_type` varchar(255),
  `body` varchar(255)
);

CREATE TABLE `user_list` (
  `ul_id` integer PRIMARY KEY,
  `u_id` integer
);

CREATE TABLE `role` (
  `rp_id` integer PRIMARY KEY,
  `ul_id` integer
);

CREATE TABLE `role_profile` (
  `rp_id` integer PRIMARY KEY,
  `r_name` varchar(255),
  `r_col` varchar(255),
  `r_desc` varchar(255),
  `p_id` integer
);

CREATE TABLE `permissions` (
  `p_id` integer PRIMARY KEY,
  `rp_id` integer,
  `se_media` boolean,
  `se_msg` boolean,
  `se_com` boolean,
  `re_msg` boolean
);

CREATE TABLE `commands` (
  `co_id` integer PRIMARY KEY,
  `b_id` integer
);

CREATE TABLE `media_collection` (
  `m_id` integer PRIMARY KEY,
  `b_id` integer
);

CREATE TABLE `report` (
  `r_id` integer PRIMARY KEY,
  `u_id` integer,
  `rt_id` integer
);

CREATE TABLE `report_type` (
  `rt_id` integer PRIMARY KEY,
  `is_med` boolean,
  `is_msg` boolean,
  `is_usr` boolean,
  `is_srv` boolean,
  `is_chl` boolean,
  `is_oth` varchar(255)
);

ALTER TABLE `users` ADD FOREIGN KEY (`u_id`) REFERENCES `accounts` (`a_id`);

ALTER TABLE `messages` ADD FOREIGN KEY (`u_id`) REFERENCES `users` (`u_id`);

ALTER TABLE `message_content` ADD FOREIGN KEY (`b_id`) REFERENCES `messages` (`b_id`);

ALTER TABLE `channels` ADD FOREIGN KEY (`c_id`) REFERENCES `messages` (`c_id`);

ALTER TABLE `servers` ADD FOREIGN KEY (`owner_user_id`) REFERENCES `users` (`u_id`);

ALTER TABLE `channels` ADD FOREIGN KEY (`se_id`) REFERENCES `servers` (`se_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`u_id`) REFERENCES `user_list` (`u_id`);

ALTER TABLE `user_list` ADD FOREIGN KEY (`ul_id`) REFERENCES `servers` (`se_id`);

ALTER TABLE `role_profile` ADD FOREIGN KEY (`p_id`) REFERENCES `permissions` (`p_id`);

ALTER TABLE `role_profile` ADD FOREIGN KEY (`rp_id`) REFERENCES `role` (`rp_id`);

ALTER TABLE `commands` ADD FOREIGN KEY (`b_id`) REFERENCES `message_content` (`b_id`);

ALTER TABLE `media_collection` ADD FOREIGN KEY (`b_id`) REFERENCES `message_content` (`b_id`);

ALTER TABLE `report` ADD FOREIGN KEY (`rt_id`) REFERENCES `report_type` (`rt_id`);

ALTER TABLE `report` ADD FOREIGN KEY (`u_id`) REFERENCES `users` (`u_id`);

ALTER TABLE `role` ADD FOREIGN KEY (`ul_id`) REFERENCES `user_list` (`ul_id`);
