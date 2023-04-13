int main(){
    int a;
    int b;
    int soma;
    printf('Digite o valor de a');
    scanf('%d', a);
    printf('Digite o valor de b');
    scanf('%d', b);
    soma = a + b;
    printf('a + b = %d', soma);
    if (!(soma>10) && (a!=10))
    {
        printf('Soma maior que 10 AAAAAAAAAAAAAA');  
    }else{
        printf('Soma menor que 10');
    }
    if(soma>10){
        printf('Soma maior que 10');
    }
    int i;
    for (i = 0; i < 10; i++)
    {
        printf('i = %d', i);
    }
    
    
    return;
}