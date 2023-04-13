int main(){
    int a;
    int b;
    int soma;
    printf('Digite o valor de a');
    scanf('%d', a);
    printf('Digite o valor de b');
    scanf('%d', b);
    if(a>0 && b>0){
        soma = a + b;
        printf('%d + %d = %d', a, b, soma);
    }
    else{
        printf('Valores invalidos');
    }
    return;
}