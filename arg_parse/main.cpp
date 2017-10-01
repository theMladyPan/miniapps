#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char ** argv){

	vector<string> args;
	const string exe_name = argv[0];
	args.assign(argv+1, argv+argc);

  uint16_t local_arg1;
  string *local_arg2 = new string();

	for(vector<string>::iterator it = args.begin();it!=args.end();it++){ //iterate throught all arguments
		if(*it=="-arg1"){
			local_arg1 = atoi((*(++it)).c_str()); // assing number after -arg1 to local_arg1
			}
		else if(*it=="-arg2"){
			*local_arg2 = *(++it); // assing string after -arg2 to local_arg2
			}
		/*
    continue like this...
    */

		else{
			cerr<<"Invalid argument: "<<*it<<endl;
			return 1;
			}
		}

    /*now you have all your arguments parsed */

}
