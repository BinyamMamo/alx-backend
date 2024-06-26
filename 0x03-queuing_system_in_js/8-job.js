import { Queue, Job } from 'kue';

/**
 * Creates a set of push notification jobs in a given queue.
 *
 * @param {Object[]} jobs - An array of job information objects.
 * @param {Object} queue - The queue to create the jobs in.
 * @throws {Error} If the `jobs` parameter is not an array.
 */
export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log(
          'Notification job',
          job.id,
          'failed:',
          err.message || err.toString()
        );
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
