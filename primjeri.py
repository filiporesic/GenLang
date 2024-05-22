from Snailplus import *

primjer1 = ('''
            program(){   // svaki program kreće sa program()
                Ispis "Primjer ";
                //primjeri za operacije na brojevima
                a = -12;
                Ispis "a = "; Ispis a;
                b = 23;
                Ispis "b = "; Ispis b;

                Ispis "a+b = "; Ispis a+b;
                Ispis "a*b = "; Ispis a*b;
                Ispis "a-b = "; Ispis a-b;
                Ispis "a/b = "; Ispis a/b;
                Ispis "a^b = "; Ispis a^b;
                Ispis "a<b = "; Ispis a<b;
                Ispis "a>b = "; Ispis a>b;
                Ispis "a>=b = "; Ispis a>=b;
                Ispis "a<=b = "; Ispis a<=b;
                Ispis "a!=b = "; Ispis a!=b;
                Ispis "a==b = "; Ispis a==b;
                Ispis "a|b = "; Ispis a|b;
                Ispis "a&b = "; Ispis a&b;
                Ispis "-b = "; Ispis -b;
                Ispis "!b = "; Ispis !b;
                Ispis "#b = "; Ispis #b;

                Vrati 1;
            }
            ''')

primjer2 = ('''
            program(){
                Ispis "Primjer 2";
                //primjeri za stog
                Stog S1;
                Stog S2;

                Push S1 1;
                Push S1 2;
                Push S1 3;
                Ispis "stog S1 = "; Ispis S1;

                Push S2 -5;
                Push S2 6;
                Push S2 2;
                Ispis "stog S2 = "; Ispis S2;

                Stog S3;
                S3 = Zbrojistogove S1 S2;
                Ispis "stog S3 je zbroj S1 i S2 = "; Ispis S3;

                Pop S3;
                Ispis "nakon operacije Pop S3 zadnji element u stogu S3 = "; Ispis Top S3;

                S3 = Merge S1 S2;
                Ispis "stog S3 je merge S1 i S2 = "; Ispis S3;

                Ispis "zbroj elemenata u S3 = "; Ispis Zbrojielemente S3;

                Ispraznistog S3;
                Ispis "prazan stog S3 nakon operacije Ispraznistog S3 = "; Ispis S3;

                Vrati 2;
            }
            ''')

primjer3 = ('''

            program(){
                Ispis "Primjer 3";
                // primjeri za tip crta
                C1 = prazno;
                C2 = kratke;
                C3 = duge;
                Ispis "C1=";
                Ispis C1;
                Ispis "C2=";
                Ispis C2;
                Ispis "C3=";
                Ispis C3;
                Ispis "Concat C1 C2 = ";
                Ispis Concat C1 C2 ; // Concat prazno kratke = kratke
                Ispis "Concat C1 C3 = ";
                Ispis Concat C1 C3; // Concat prazno duge = duge
                Ispis "Concat C2 C3 = ";
                Ispis Concat C2 C3; // Concat kratke duge = duge
                Ispis "Concat kratke C2 = ";
                C4 = Concat kratke C2 ; //mozemo i ovako s pridruzivanjem( Concat kratke kratke = duge)
                Ispis "C4 = ";
                Ispis C4;
                //jos da vidimo concat praznih
                Ispis "Concat prazno prazno = ";
                Ispis Concat prazno prazno;

                C5 = kratke;
                Ispis "C5 = ";
                Ispis C5;
                Maksimiziraj C5;
                Ispis "Maksimizirani C5 = ";
                Ispis C5;

                Isprazni C5;
                Ispis "Ispraznjen C5 = ";
                Ispis C5;

                // koliko ih ima u oba
                Ispis "C1 i C2 skupa sadrzavaju ovoliko crta:";
                Ispis Prebrojicrte C1 C2;
                Ispis "A C2 i duge(20crta) skupa sadrzavaju ovoliko crta:";
                Ispis Prebrojicrte duge C2;
                Vrati 3;
            }
            ''')

primjer4 = ('''
            //rekurzije
            unazadzadva (broj) {
                Ako broj<=0 Onda {
                    Ispis "Nula!";
                    Vrati 0;
                } Inace {
                    Ispis broj;
                    c = broj-2;
                    Vrati unazadzadva(c);
                } Akokraj
            }
            fakt (broj) {
                Ako broj==0 Onda {
                    Vrati 1;
                } Inace {
                    Vrati broj*fakt(broj-1);
                } Akokraj
            }
            fib (broj) {
                Ako broj<=1 Onda {
                    Vrati broj;
                } Inace {
                    Vrati fib(broj-1)+fib(broj-2);
                } Akokraj
            }
            sumaprvihn (n) {
                Ako n==1 Onda {
                    Vrati 1;
                } Inace {
                    Vrati n+sumaprvihn(n-1);
                } Akokraj
            }

            program(){
                Ispis "Primjer 4";
                Ispis "ispisujemo od broja 13 sve do 0 sa pomakom od 2";
                Ispis unazadzadva(13);
                Ispis "4! = ";
                Ispis fakt(4);
                Ispis "fib(14) = ";
                Ispis fib(14);
                Ispis "suma prvih 9 = ";
                Ispis sumaprvihn(9);
                Vrati 4;
            }
            ''')

primjer5 = ('''

            StogPopuni(a,b,c,d,e){
                Stog Spom;
                Push Spom a;
                Push Spom b;
                Push Spom c;
                Push Spom d;
                Push Spom e;
                Vrati Spom;
            }
            program(){
                Ispis "Primjer 5";
                Stog S1;
                Ispis "stog S1 je prazan = "; Ispis S1;

                Ispis "Popunimo ga!";
                Unos a; Unos b; Unos c; Unos d; Unos e;
                S1 = StogPopuni(a,b,c,d,e);
                Ispis S1;

                Stog S2;
                Ispis "popunimo S2";
                S2 = StogPopuni(a+b,c+d*(a<b),Zbrojielemente S1,-d,#e);
                Push S2 22/11+5;
                Ispis S2;

                Ako Size S2 > Size S1 Onda {
                    Ispis "S2 ima vise elemenata izbacimo zadnji";
                    Pop S2;
                    Ispis S2;
                } Akokraj;

                Ako 2!=3 Onda {
                    Ispis "Merge S1 i S2 = ";
                    Stog S3;
                    S3 = Merge S1 S2;
                    Ispis S3;
                } Akokraj;

                Ispis "najduzi stog = ";
                Stog S4;
                S4 = Merge S3 S1;
                Ispis Najduzi S3 S4 S1;

                Ispis "najkraci stog = ";
                Ispis Najkraci S3 S4 S1;
                Vrati 5;
            }
            ''')

primjer6 = ('''
            //implicitna pretvaranja
            StogPopuni(a,b,c){
                Stog Spom;
                Push Spom a;
                Push Spom b;
                Push Spom c;
                Vrati Spom;
            }

            Crte(){

                a = 10;
                Vrati a; // a ce se implicitno pretvoriti u tip crta

            }
            program(){
                Ispis "Primjer 6";
                Ispis Crte();

                Stog S1;
                Unos S1;
                Ispis "S1="; Ispis S1;
                a = S1; //S1 se pretvara u broj(zbroj njegovih elemenata)
                C = S1; //S1 se pretvara u tip crta

                Ispis "a=";Ispis a;
                Ispis "C="; Ispis C;

                Stog S2;
                Push S2 S1;// S1 se pretvara u broj pa se takav dodaje u stog
                Ispis "S2=";
                Ispis S2;

                Unos C1; //primjer unosenja crta(ako se ne unese neka od kljucnih rijeci, vrijednost u varijabli je prazno)
                Ispis "C1=";Ispis C1;

                zbroj = kratke + S2 + 4; //sve ce se implictno pretvoriti (kratke u 10, S2 u zbroj svojih elemenata)
                Ispis "kratke + S2 + 4= ";Ispis zbroj;
                Ispis duge;

                S3 = StogPopuni(4,C1,S1); //C1 i S1 ce se implicitno pretvoriti
                Ispis "S3=";Ispis S3;

                Ispis duge;

                Ispis "Funkcija Stog popuni vraca: "; Ispis StogPopuni(2,3,-11);
                b = StogPopuni(2,3,-11); //F-ja ce vratiti stog koji ce se pretvoriti u broj

                Ispis "A kada ju pridruzimo b-u iznosi"; Ispis b;

                Ispis duge;

                Ispis "Izraz 4*2-10^2-8+!(6>3) = "; Ispis 4*2-10^2-8+!(6>3);
                S5 = 4*2-10^2-8+!(6>3); //izraz postaje stog
                Ispis "a kad ga pridruzimo stogu postaje: "; Ispis S5;


                Vrati 6;
            }
            ''')

primjer7 = ('''

            program(a){
                Ispis "Primjer 7";
                Unos b;

                Test (a < b) ? {a = -5; Ispis a; } : Ispis b; /* ovo
                je
                komentar
                kroz više
                linija sa naredbom Ispis "marko";
                koja se ignorira */

                Ispis Newline;

                Test (a*4-6 < b^2/11) ? Ispis a : Ispis b;

                Vrati 7;
            }
            ''')



primjeri = [primjer1, primjer2, primjer3, primjer4,primjer5, primjer6]
for primjer in primjeri:
    print(primjer)
    sn(primjer)
    prikaz(P(primjer))
    izvrši(P(primjer))

izvrši(P(primjer7),5) #poziv s komandne linije
