import mysql from 'mysql2/promise'

import {config} from 'dotenv'
config()

const pool = mysql.createPool({
    hostname:process.env.HOSTNAME,
    user: process.env.USER,
    password :process.env.PASSWORD ,
    database: process.env.DATABASE
})

const getShopleft =async () => {
    let data = await pool.query('SELECT * FROM products')
    return data
}

console.log(await(getShopleft()));

// a. Create a function that returns all the users.
const getUsers =async () => {
    let data = await pool.query('SELECT * FROM users')
    return data
}

console.log(await(getUsers()));

const deleteProducts = async (product_code) => {
    let data = await pool.query('DELETE FROM products WHERE product_code= ?',[product_code]);
    return data
}
console.log(await deleteProducts('baro1'));

const patchProducts = async (product_code,product_name,product_price,product_quatity) => {
    let [data] = await pool.query('INSERT INTO products (product_code, product_name, product_price, product_quatity) VALUES (?, ?, ?, ?)', [product_code, product_name, product_price, product_quatity])

    return data
}
console.log(await patchProducts('bur1','burger','55.99',5));

const updateProduct = async (product_code,product_name,product_price,product_quatity) => {
    let [data] = await pool.query('UPDATE products SET product_code =? , product_price =? , product_quatity=?  WHERE product_name= ?',[product_code,product_name,product_price,product_quatity])
    return data 
}
console.log(await updateProduct('jik1','25.99',4,'albex'));
