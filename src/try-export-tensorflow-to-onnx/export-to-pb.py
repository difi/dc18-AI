import tensorflow as tf
import os

modelname = os.path.join("models", "model");

meta_path = modelname + ".ckpt.meta"
output_node_names = ['outputs']

with tf.Session() as sess:

    # Restore the graph
    saver = tf.train.import_meta_graph(meta_path)

    # Load weights
    saver.restore(sess,tf.train.latest_checkpoint('models'))

    # Freeze the graph
    print("SESSION GRAPH DEF:")
    print(sess.graph_def)
    
    frozen_graph_def = tf.graph_util.convert_variables_to_constants(
        sess,
        sess.graph_def,
        output_node_names)
    
    print("FROZEN GRAPH DEF:")
    print(frozen_graph_def)

    # Save the frozen graph
    with open(modelname + ".pb", 'wb') as f:
      f.write(frozen_graph_def.SerializeToString())
