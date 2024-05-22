from genetika import *

kod1= P('''
---prvi kod ce prikazivati funkcionalnosti petlji, grananja i funkcija
    y=0;
    output("ispis iz glavnog programa 1");
    f=function(x){
    if(x>=1){
        if(x<=3){
        y=x;
        output("ispis iz prve funckije");
        output(y);
        }
    }
        
    };
    g=function(x){
    output("ispis iz druge funckije");
    output(x);
    call.f(x);
    };
    for(i=1; i<8; i++){
    call.g(i);
    }
    output("ispis iz glavnog programa 2");
    if(y==0){
    output("y se nije promjenio");
    }
    if(y!=0){
    output("y se promjenio, a to ne zelimo");
    }
    h=function(){
    x="ova funkcija ima povratnu vrijednost";
    return x;
    };
    z=call.h();
    output(z);
       ''')
kod2= P('''
---drugi kod ce preko outputa procitati ime filea, nakon toga ce u njemu procitati procitati 
---ime filea koji sadrzi podatke za analizu, te cemo nakon toga izracunati postotak pojavljivanja
---bolesti tipa Benign i ucinka missense_variant, ucitane iz iste datoteke, te cemo ih spremiti 
---u polje koje cemo potom ispisati iteracijom kroz elemente polja
        x = "proba.txt";
        file = open(x, "r");
        data = READOPTION(file, line);
        x=variant(data);
        percentages=collection();
        disease = READOPTION(file, line);
        consequence = READOPTION(file, line);
        y = diseasePercentage.x(disease);
        z = consequencePercentage.x(consequence);
        append.percentages(y, z);
        sz=size.percentages();
        for(i=0; i<sz; i++){
        output(percentages[i]);
        }
        close(file);
       ''')

kod3= P('''
       x=gen("ATC");
       y=gen("ACC");
       foo = function(x,y){
       x=x+y;
       output(x);
       x=[x,y];
       output(x);
       };
       output(x);
       output(y);
       ---obzirom da je mutacija nasumicna, moguce je da dobijemo ponovno isti gen
       y=mutation(x);
       ---~y;
       output(x);
       output(y);
       ~y;
       output(y);
       mutation(y);
       output(y);
       z=x%y;
       output(z);
       call.foo(x,y);
       ''')


prikaz(kod1,8)
kod1.izvrši()

prikaz(kod2,8)
kod2.izvrši()

prikaz(kod3,8)
kod3.izvrši()


#implementacija Smith–Waterman algoritma
#algoritam je slican vec implementiranom operatoru za slicnost gena ali radi za vecu kolekciju
#
zad= P('''
        ---popis dozvoljenih kiselina
        file = open("acids.txt", "r");
        ak1 = READOPTION(file);
        ak = split(ak1);
        close(file);
        ---tablica vrijednosti za poravnanja
        file = open("blosum50.txt", "r");
        bm=collection();
        for(i=0; i<20; i++)
        {
            redak = READOPTION(file, line);
            vc = split(redak);
            append.bm(vc);
        }
        x1 = gen("P E W");
        x = split(x1);
        y1 = gen("G A L A P A W A L A");
        y = split(y1);
        m = 3; 
        n = 10;
        sm = collection();
        maks = 0;
        ii = 0;
        jj = 0;

        m1 = m+1;
        n1 = n+1;
        for(i=0; i<n1; i++)
        {
            tmp = collection();
            for(j=0; j<m1; j++)
            {
                append.tmp(0);
            }
            append.sm(tmp);
        }
        
        ---score matrica
        for(i=1; i<n1; i++)
        {
            for(j=1; j<m1; j++)
            {
                tmp1 = collection();
                i1=i-1;
                j1=j-1;
                vrijednost = sm[i1][j];
                vrijednost2 = vrijednost-8;
                append.tmp1(vrijednost2);
                vrijednost = sm[i][j1];
                vrijednost2 = vrijednost-8;
                append.tmp1(vrijednost2);
                kiselina1 = y[i1];
                kiselina2 = x[j1];
                for(k=0; k<20; k++)
                {
                    if(ak[k]==kiselina1)
                    {
                        ind1 = k;
                    }
                    if(ak[k]==kiselina2)
                    {
                        ind2 = k;
                    }
                }
                bb=bm[ind1][ind2];
                vrijednost3 = sm[i1][j1]+bb;
                append.tmp1(vrijednost3);
                append.tmp1(0);
                sort.tmp1();
                sm[i][j] = tmp1[3];
                if(sm[i][j]>maks)
                {
                    maks = sm[i][j];
                    ii=i;
                    jj=j;
                }
            }
        }
        str1 = collection();
        str2 = collection();

        output("Score matrica izgleda ovako:");
        for(i=0; i<n1; i++)
        {
            output(sm[i]);
        }

        ---traceback, vracamo se od kraja i provjeravamo vrijednosti kako bi nasli optimalno poravnanje
        i=ii;
        j=jj;
        for(l=0; l<10;l++)
        {
            l = l-1;
            if(i<=0)
            {
                break;
            }
            if(j<=0)
            {
                break;
            }
            if(sm[i][j]==0)
            {
                break;
            }
            n1=sm[i][j]+8;
            vrijednost1=i-1;
            if(sm[vrijednost1][j]==n1)
            {
                if(i>0)
                {
                    vrijednost2=j-1;
                    append.str1(y[vrijednost2]);
                    vrijednost3 = 0-100;
                    append.str2(vrijednost3);
                    i=i-1;
                }
            }
            vrijednost1=j-1;
            if(sm[i][vrijednost1]==n1)
            {
                if(j>0)
                {
                    vrijednost2=j-1;
                    append.str1(x[vrijednost2]);
                    vrijednost3 = 0-100;
                    append.str2(vrijednost3);
                    i=i-1;
                }
            }
            vrijednost1=j-1;
            if(sm[i][vrijednost1]!=n1)
            {
                vrijednost1=i-1;
                vrijednost1 = i-1;
                vrijednost2 = y[vrijednost1];
                append.str2(vrijednost2);
                vrijednost1 = j-1;
                vrijednost2 = x[vrijednost1];
                append.str1(vrijednost2);
                i=i-1;
                j=j-1;
            }
            if(i<=0)
            {
                vrijednost1=i-1;
                vrijednost1 = i-1;
                vrijednost2 = y[vrijednost1];
                append.str2(vrijednost2);
                vrijednost1 = j-1;
                vrijednost2 = x[vrijednost1];
                append.str1(vrijednost2);
                i=i-1;
                j=j-1;
            }
            if(sm[vrijednost1][j]!=n1)
            {
                vrijednost1=i-1;
                vrijednost1 = i-1;
                vrijednost2 = y[vrijednost1];
                append.str2(vrijednost2);
                vrijednost1 = j-1;
                vrijednost2 = x[vrijednost1];
                append.str1(vrijednost2);
                i=i-1;
                j=j-1;
            }
            if(j<=0)
            {
                vrijednost1=i-1;
                vrijednost1 = i-1;
                vrijednost2 = y[vrijednost1];
                append.str2(vrijednost2);
                vrijednost1 = j-1;
                vrijednost2 = x[vrijednost1];
                append.str1(vrijednost2);
                i=i-1;
                j=j-1;
            }
        }
        reverse.str1();
        reverse.str2();
        duljina1 = size.str1();
        duljina = duljina1 - m;
        for(i=0; i<duljina; i++)
        {
            removeIndex.str1(0);
            removeIndex.str2(0);
        }
        output("Optimalno poravnanje");
        output(str1);
        output(str2);
       ''')

prikaz(zad,8)
zad.izvrši()
