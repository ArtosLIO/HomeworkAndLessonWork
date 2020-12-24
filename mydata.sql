--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id integer NOT NULL,
    film character varying(100) NOT NULL,
    director character varying(100) NOT NULL,
    actors text[] NOT NULL,
    release_date date NOT NULL
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: films_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO postgres;

--
-- Name: films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;


--
-- Name: films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (id, film, director, actors, release_date) FROM stdin;
1	Џ а  ­  Їа §¤­ЁЄЁ	„¦®­ “ ©вбҐ««	{"ќ¬¬  ђ®ЎҐавб","‹оЄ Ѓа ©бЁ","ЉаЁбвЁ­ —Ґ­®ўҐв"}	2020-10-28
3	•Ёй­лҐ ЇвЁжл	ЉнвЁ џ­м	{"Њ аЈ® ђ®ЎЎЁ","ЊнаЁ ќ«Ё§ ЎҐв “Ё­бвн¤","„¦Ґа­Ё ‘¬®««Ґвв"}	2020-01-29
2	Ѓ« ¤и®в	David S F Wilson	{"‚Ё­ „Ё§Ґ«м","ѓ © ЏЁаб","’ «г«  ђ ©«Ё"}	2020-02-21
\.


--
-- Name: films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

