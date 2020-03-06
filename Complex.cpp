#include "Complex.h"
#include <bits/stdc++.h>

Complex::Complex(int r=0, int i=0): r(r),i(i){}
 int Complex::get_r()const{return r;}
 int Complex::get_i()const{return i;}
 void Complex::afisare()const{std::cout<<r<<"+"<<i<<"*i";}
 std::string Complex::afisare2()const{std::string s; s+=std::to_string(r)+"+"+std::to_string(i)+"*i"; return s;}
