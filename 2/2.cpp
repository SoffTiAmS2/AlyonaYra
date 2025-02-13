#include<iostream>
#define ll long long

template <typename T> 
struct Arra{
    T* data;
    ll size;


    Arra(){
        data = new T[size];
    }


    ~Arra(){
        delete[] data;
    }


    void push_back(const T& value) {
        T* new_date = new T[size+1];
        for (int i = 0; i < size; i++)
            new_date[i] = this->date[i]; 
        data[size++] = value;
        delete[] this->data;
        this->data = data;
    }

    Arra(int size, int chem = NULL){
        data = new T[size];
        this->size = size;
        if(chem != NULL){
            for (int i = 0; i < size; i++)
                data[i] = chem;
        }
    }
}; 