class DynamicArray {
    private int[] myArray;
    private int size = 0;

    public DynamicArray(int capacity) {
        myArray = new int[capacity];
    }

    public int get(int i) {
        return myArray[i];
    }

    public void set(int i, int n) {
        myArray[i] = n;
    }

    public void pushback(int n) {
        if (getSize() == getCapacity()) {
            resize();
        }
        myArray[getSize()] = n;
        size++;
    }

    public int popback() {
        if (size == 0) {
            throw new ArrayIndexOutOfBoundsException("Array is empty");
        }
        int value = myArray[size - 1];
        myArray[size - 1] = 0; // Optionally clear the value (though not strictly necessary)
        size--;
        return value;
    }


    private void resize() {
        int newArray[] = new int[2 * myArray.length];
        System.arraycopy(myArray, 0, newArray, 0, myArray.length);
        myArray = newArray;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return myArray.length;
    }
}
