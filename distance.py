class Distance:
    """
    A class used to sort and clean distance data and return a list
    to be used for finding the distances from address to address.

    TOTAL:
    -----------------------
    |  RUNTIME -> O(kn)  |
    -----------------------

    """

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.distance_table = []
        self.labels = []

    def clean_and_sort_data(self):
        """
        - grab the first row of data as our labels/sub-keys
        - get rid of blank spots
        - while raw data still has values organize that into a clean list
        - use the first label as key
        - then use the sub-keys to find the distance from key
        - see details of each line for more info

        -----------------------
        |  RUNTIME -> O(kn)  |
        -----------------------

        :return: return a clean distance data list
        """
        self.labels = self.raw_data.pop(0)  # remove our label elements from the raw data list

        for i in self.labels:  # more cleaning of labels
            if i == '':
                self.labels.remove(i)  # get rid of any blank labels

        count = len(self.raw_data) - 1  # start counter
        while len(self.raw_data) != 0:  # while raw data list has values in it

            popped_data = self.raw_data.pop(0)  # remove the data at front of the list

            temp_key = []  # temporary key list
            temp_sub_key_val_pair = []  # temporary sub-key / value pair list

            label_counter = 0  # keep track of what label we are using as a sub-key
            for i in popped_data:
                if i == popped_data[0]:  # if the item is equal to the key
                    temp_key = i  # our main key

                else:  # otherwise we assign sub-key value pairs

                    temp_sub_key = self.labels[label_counter]  # temporary sub-key
                    temp_value = i  # temporary distance value

                    skvp = temp_sub_key, temp_value  # temporary list of sub-key value pair

                    temp_sub_key_val_pair.append(list(skvp))  # append to our temp list
                    label_counter += 1

                if label_counter == len(self.labels) - 1:  # if at the end of our label list
                    kvp = temp_key, temp_sub_key_val_pair  # official key value pairs
                    self.distance_table.append(list(kvp))  # add our cleaned data to distance table

            count -= 1

        return self.distance_table

    def get_labels(self):
        return self.labels
