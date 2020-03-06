#ifndef COMPLEX_H_INCLUDED
#define COMPLEX_H_INCLUDED
#include <string>
class Complex{
private:
        int r,i;
public:
    Complex (int , int);

 int get_r()const;
 int get_i()const;
 void afisare()const;
 std::string afisare2()const;
};

#endif // COMPLEX_H_INCLUDED
