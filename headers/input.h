//
// Created by pmfer on 22/02/2021.
//
#ifndef CV_DETECTION_INPUT_H
#define CV_DETECTION_INPUT_H

#include <string>
using namespace std;
class input{
    private:
        string entrypoint;
    public:
        input();
        input(string entry);
        ~input();
        string get_entrypoint();
        void set_entrypoint(string entry);
    };

#endif //CV_DETECTION_INPUT_H
