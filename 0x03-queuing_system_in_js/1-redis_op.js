import redis from 'redis';

const client = redis.createClient({
  port: 6379,
  host: '127.0.0.1',
});

client
  .on('connect', () => {c
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
  })
  .on('ready', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
  });

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log(value);
  });
}
