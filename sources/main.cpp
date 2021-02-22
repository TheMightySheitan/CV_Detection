//
// Created by pmfer on 22/02/2021.
//

#include <iostream>
#include"../headers/input.h"

using namespace std;
int main()
{
    system("screenfetch");
    cout<<"Hello from Cmake!"<<endl;
    input video = input("file.mp4");
    cout<<video.get_entrypoint()<<endl;


}


