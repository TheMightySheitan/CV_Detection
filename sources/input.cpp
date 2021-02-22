//
// Created by pmfer on 22/02/2021.
#include "../headers/input.h"
#include <iostream>
#include <string>

using namespace std;

input::input() {

}

input::input(string entry) {
    this->entrypoint=entry;
}

input::~input() {
    cout<<"Instance détruite"<<endl;

}

string input::get_entrypoint() {
    return this->entrypoint;
}

void input::set_entrypoint(string entry) {
    this->entrypoint=entry;
}