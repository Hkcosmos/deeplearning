import tensorflow

print("hello")

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess)