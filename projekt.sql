-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 09 Maj 2022, 16:03
-- Wersja serwera: 10.4.22-MariaDB
-- Wersja PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `projekt`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth`
--

CREATE TABLE `auth` (
  `ID` int(11) NOT NULL,
  `email` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `hash` varchar(512) COLLATE utf8_polish_ci NOT NULL,
  `salt` char(128) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `auth`
--

INSERT INTO `auth` (`ID`, `email`, `hash`, `salt`) VALUES
(4, 'asdassda@dddasa.com', '54cd21816cde534f603d4be78661c2d7512f40ef36531c0daef32554721d5ace6260a6cacdc4a16d5e387bfb7ac4bd01db44113fc322750370ed5ede837b560c5522d2edfe29b8fb3298c7935af409ac869be4a9d7812eff97e1c6a696516c3de6ecf08fa282f95d8ee6be40a0c63dec14881cc7880d637c4ee3075e46bee1ad54e75700f24d673ef02d44061e5e7f6a1f2079cd426cc4b6e6af880d19a8d4e0a275d06e156cdb41f8a4aea783ec2423c655f9b866afe6ddf262de57fb2237fd8303803719b628d8c6e1bad8ec8d82b6f2e6d45fe0eab0b0ce232f8d8c4a1a71a4d714fefcd4cd29546c2a633f408b0ee55cf5498f2fa93c8441ab65d74a0afb', '5fd61d0aae76428249a8d4ab38555ba6eeab4e4ff6b75a372a00a81bb794fc4aa3d5fbe40439d3d9d6e2410723ad1642b466f652282ccf4a0e268e52136d6456'),
(5, 'anczokbartek@gmail.com', '8e4384935331e0d8591a8ea365a147d2686d198558d3d6648e1b38c82ce632335675633b88177ddc59fe9d2d5416a6927d07c7c8234c354cc7fe457797fd1109ba91ae7f060e1ed0361b2eaa43ca909a6070e09143f944146570a48abb87cadef2d7cf496569580af26ab81548cceb1c3ce0321b7c4bccf3228cda3c9f94e943e65136bfe3398f85367556312367ae330a37f9acbf9bc8f749b82cde9c4e90ce816e88401013bb5ca7f1fb736223a03544871564a08fca4b1babc276a87c466d6a6287297a74d406586741108a1f4a0df9b442b990cc6881035ff46e7b97b7add3eee841785bcd8f8c38147e4117799791dd95e6bd9156446a8fd621ec06dc6c', '65ead9e027dd12d59115e388f081844ca1f2a5ded1eb067f66f06b3c7b9463b24ad1da591d01d18550542374836d301f9236c4e4fe5a8fc6d26cd0ee9cd25a0b');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `email` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `question` int(11) NOT NULL,
  `answer` text COLLATE utf8_polish_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `connections` text COLLATE utf8_polish_ci NOT NULL,
  `token` varchar(256) COLLATE utf8_polish_ci DEFAULT NULL,
  `token_timestamp` timestamp NULL DEFAULT NULL,
  `error_login_number` int(11) DEFAULT 0,
  `last_error_timestamp` timestamp NULL DEFAULT NULL,
  `new_connection_token` varchar(300) COLLATE utf8_polish_ci DEFAULT NULL,
  `connection_token_timestamp` timestamp NULL DEFAULT NULL,
  `user_token` text COLLATE utf8_polish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`email`, `question`, `answer`, `name`, `surname`, `connections`, `token`, `token_timestamp`, `error_login_number`, `last_error_timestamp`, `new_connection_token`, `connection_token_timestamp`, `user_token`) VALUES
('anczokbartek@gmail.com', 1, 'adsfs', 'badsfsd', 'adsfasdfasd', '127.0.0.1;', NULL, NULL, 0, NULL, NULL, NULL, '32fcacb95bebc3164bb1a998caab74ec4785a1c710042099294f47c2113ed1a40f0b214d258d4c6bf2f4c3979228d49863bdb911a9082836753057d18a6386582e837ce76baa2dc392356a3b959c003191f0de9b831a279d2647ba88842c3f7a44ceb4f70ff52d589368bad666108a380e65f54908be10175b699fcb8a592684'),
('asdassda@dddasa.com', 2, 'adasdasddas', 'Bartek', 'asdasd', '127.0.0.1;', NULL, NULL, 0, NULL, NULL, NULL, '86679e9902b4c6b06524875dd33299257412fd1d3410e87bbb073ada9bf3e1c40e2bc5d898771c8760904a6861a3b8193168c3b8d7c683beecb35efc9648c3508430805aea0924a83ab1cf25479824a0be12997014b95f344b3affe37fe631eb109d726404474850b53d7c803f8850749f2039c042c631d5c0d3680e8a810530');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users_data`
--

CREATE TABLE `users_data` (
  `ID` int(11) NOT NULL,
  `email` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `site` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `password` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `iv` text COLLATE utf8_polish_ci NOT NULL,
  `allowed` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `users_data`
--

INSERT INTO `users_data` (`ID`, `email`, `site`, `password`, `iv`, `allowed`) VALUES
(13, 'asdassda@dddasa.com', 'sasdfadsfasd', '00KeifLaIG9CsmRoItksbeiimPrV2Rihe+Z+kelGaPw=', 'Qr6YY/4NXW637MPWkoI8Jw==', 'anczokbartek@gmail.com;'),
(15, 'asdassda@dddasa.com', 'xczxcxzc', 'bdcqLev+nyZcmoc5uiFQFOiOU7X7JuaaIirYQM01m9s=', 'I0/tQo8HRUpwYotyHMpkGQ==', 'anczokbartek@gmail.com;'),
(16, 'anczokbartek@gmail.com', 'gs', 'JEYsCPcpCYLErKqllZZloMKNoJnY8uCoFx9z2tEoj8o=', 'UPT2qpcf1hmLpenI06/jEQ==', 'asdassda@dddasa.com;'),
(17, 'anczokbartek@gmail.com', 'adfasdfsadf', '/Gb2oAlzzQX4pjHSvndp/eQiqdpMPhe4GVwUkyPPEz8=', 'GKw/hjvyKYwGbKRscuOONA==', ';'),
(18, 'anczokbartek@gmail.com', 'adfasdfsadf1', 'qZeu2d7PbzG9UAIXkErMGDhKikS+/S6Jx7tL3iaANgg=', 'L9dmiD3r2VgVBqmTplUN+A==', ';'),
(19, 'anczokbartek@gmail.com', 'test', 'rTY4kADBI/IazAD8Q6gkTA==', 'ppaVYB+CokFMu1rCsRQKyQ==', ';'),
(20, 'anczokbartek@gmail.com', 'adfasfasdfas', 'OcjB0gIBMSsw3CtDTW0Fdlid+HA2xgbdtxm3EvUcZtE=', '6X/PMvNL1Pv2o0lH+LXtOQ==', ';'),
(21, 'anczokbartek@gmail.com', 'testetst', '6tJ9K1f58vray18+4E7LMBxOOh4kXO5JuDquWLXb+JA=', 'grtcPNA4O/8Y+cPbPLC1vg==', ';'),
(22, 'asdassda@dddasa.com', 'dfasdfasdfa', 'EG3tPNygWE1RE8w6IA+89jFP1szQRdCCbXuGqyO2AXQ=', '8GWv6yBqbBR5ryusq1pnTg==', ';'),
(23, 'asdassda@dddasa.com', 'test123', 'Pde28rDim+OBvrhJ2Or+rGqRg2gMNk/RHeXtMhgYb1s=', 'hoCjFqvZfhioBt6vEEFrfw==', 'anczokbartek@gmail.com;'),
(24, 'asdassda@dddasa.com', 'test12312341234', 'U5pMjpwJfTnwQeD233e17X2NG6N1eNY7bHtL+URiwnk=', 'eiLVXaWjviZqj/QKXjWNeg==', 'anczokbartek@gmail.com;'),
(25, 'asdassda@dddasa.com', '12341234', '0dGC5PQIUw0GyAbtLBoGWQiP1MCWOM1uJJeqS2x3www=', 'zitfpfJYJn4d1ULHh75Iag==', ';'),
(26, 'anczokbartek@gmail.com', '12341234123412341234123', '2EQ2ZbrpUHuDxjQ2eZyEYsd4xSWLMrN8lH5XiNUV1co=', 'sEDOydq41ibRNm/oURcUdg==', 'asdassda@dddasa.com;'),
(27, 'anczokbartek@gmail.com', '1aaa1234123', '7VR2zOBlNnEuI8OjZw/Yi7Rpn6AWH5HZ7ljiN/sb0OE=', '3DX1LXohx4i6RbIbFk2SAA==', ';'),
(28, 'anczokbartek@gmail.com', 'abcd', 'V45U7aox94KyTvT+LE/gff7BG4f/f0+f7MqZd9UT1IA=', 'thx2T/h5Rrf5lQnx/UkecQ==', ';'),
(29, 'anczokbartek@gmail.com', '1111', 'K2aohPDuphjBrYCqnAiJd44qjUHWLblClhxdsSASBIs=', '44dV4eZ2E1UBrayWBw99/g==', ';'),
(30, 'asdassda@dddasa.com', 'test 123', 'zN1PHbZBFbWo8J60cKZbXNkFMG86V9GoidAGizD2GIw=', '92oTunBvZsVpZBDhfHi0NQ==', ';'),
(31, 'asdassda@dddasa.com', 'abc123', '7pd+wZfxTKPnwiSRJDO3jeIAttZj+V0tVrT5KOu2yaM=', '8AOMc7eSu4W0P6LnN6LeOw==', ';'),
(32, 'anczokbartek@gmail.com', 'dfdsfgsdgsd', 'XzbXrXoz1uyKGLp+kNG8Lf2z5c2/dD84qTAa7316bug=', '0SoLM0C7BbWekrNnNSq96Q==', ';'),
(33, 'anczokbartek@gmail.com', 'TESTETS', 'WaROKxgo4Sb+3446AzBtYg==', 'emoYahc8TuzmJEsdJThfOg==', 'aaaa@aaaa.com;'),
(34, 'anczokbartek@gmail.com', 'adsfdsfas', 'LnyfpARYAtOArATCfObvsTCsY6VZoe/fxl34bcbOZUM=', 'A8SQQklTSXkT40FlY8qOaA==', ';');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `auth`
--
ALTER TABLE `auth`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `email` (`email`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- Indeksy dla tabeli `users_data`
--
ALTER TABLE `users_data`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_users_data` (`email`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `auth`
--
ALTER TABLE `auth`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `users_data`
--
ALTER TABLE `users_data`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `auth`
--
ALTER TABLE `auth`
  ADD CONSTRAINT `FK_users_auth` FOREIGN KEY (`email`) REFERENCES `users` (`email`);

--
-- Ograniczenia dla tabeli `users_data`
--
ALTER TABLE `users_data`
  ADD CONSTRAINT `FK_users_data` FOREIGN KEY (`email`) REFERENCES `users` (`email`);

DELIMITER $$
--
-- Zdarzenia
--
CREATE DEFINER=`root`@`localhost` EVENT `event_del_pass_token` ON SCHEDULE EVERY 30 SECOND STARTS '2022-01-17 20:33:09' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `users` SET token = NULL WHERE token_timestamp < DATE_SUB(NOW(), INTERVAL 15 MINUTE) AND token IS NOT NULL$$

CREATE DEFINER=`root`@`localhost` EVENT `event_del_conn_token` ON SCHEDULE EVERY 30 MINUTE STARTS '2022-01-17 20:34:27' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `users` SET new_connection_token = NULL WHERE connection_token_timestamp < DATE_SUB(NOW(), INTERVAL 1 DAY) AND new_connection_token IS NOT NULL$$

CREATE DEFINER=`root`@`localhost` EVENT `event_del_log_token` ON SCHEDULE EVERY 30 SECOND STARTS '2022-01-17 20:35:10' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE `users` SET error_login_number = 0 WHERE last_error_timestamp < DATE_SUB(NOW(), INTERVAL 15 MINUTE) AND  error_login_number >= 5$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
