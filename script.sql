create table transactions( transaction_date DATE, transaction_hour INTEGER, transaction_value REAL, created_date DATETIME);
create index idx_date on transactions(transaction_date, transaction_hour);
