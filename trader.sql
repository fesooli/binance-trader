create database trader;

create table BinanceTRXPrices (
	trx_id int primary key DEFAULT nextval('"BinanceTRXPrices_sequence"'::regclass),
	trx_price numeric(15,4) NOT NULL DEFAULT 0.00,
	trx_minute_date timestamp not null
);

CREATE SEQUENCE "BinanceTRXPrices_sequence"
INCREMENT BY 1
MINVALUE 1
MAXVALUE 9223372036854775807
START 1;

drop table public.binancetrxprices;

INSERT INTO public.binancetrxprices (trx_price, trx_minute_date) VALUES(0.00, '');

select * from public.binancetrxprices;