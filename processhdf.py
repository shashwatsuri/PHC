import ezc3d
import pickle

def c3d_to_pkl(c3d_filepath, pkl_filepath):
    # Step 1: Read the C3D file using ezc3d
    c3d = ezc3d.c3d(c3d_filepath)
    
    # Extracting marker data (positions) as an example
    # Note: You may want to extract other data like analog, events, etc., based on your needs
    marker_data = c3d['data']['points']
    
    # Step 2: Serialize the extracted data to a .pkl file
    with open(pkl_filepath, 'wb') as pkl_file:
        # Using highest protocol for efficiency
        pickle.dump(marker_data, pkl_file, protocol=pickle.HIGHEST_PROTOCOL)

# Example usage
c3d_filepath = 'sample_data/walking.c3d'
pkl_filepath = 'sample_data/walking.pkl'
c3d_to_pkl(c3d_filepath, pkl_filepath)
