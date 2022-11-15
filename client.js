const { Client } = require('pg');

const pgclient = new Client({
    host: '127.0.0.1',
    port: '5432',
    user: 'postgres',
    password: 'postgres',
    database: 'dgen_db'
});

pgclient.connect();
