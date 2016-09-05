//Método do scanf: scanf("%tipo", &variável)
//Variáveis necessárias para o funcionamento do código:
char *nickname[20];
char *log_cut_type[30];
char *type_normal[6];
char *type_oak[8];
char *type_willow[9];
char *type_teak[4];
char *type_maple[5];
char *type_mahogany[8]; //OBS.: Para facilitar o reaproveitamento do código, o nº de caracteres será o maior (entre pt e en).
char *type_arctic_pine[16];
char *type_eucalyptus[10];
char *type_yew[5];
char *type_ivy[4];
char *type_magic[6];
char *type_blisterwood[12];
char *type_cursed_magic[18];
char *type_mutated_vine[12];
char *type_curly_straight_root[10];
char *type_ancient[7];
char *type_crystal[7];
int ability;
int ability_level;
float xp_qnt;
int ret1;
int ret2;
int ret3;
int ret4;
int ret5;
int ret6;
int ret7;
int ret8;
int ret9;
int ret10;
int ret11;
int ret12;
int ret13;
int ret14;
int ret15;
int ret16;
int ret17;




//Protótipo de funções:
void program_title();
void sys_lang();//50% - Serve pra acentuar em pt_BR, nesse caso!
void receive_nickname(); //OK
void receive_ability_name(); //30%
void receive_ability_level();// OK
void check_level();// OK
void check_quantity_of_exp();
void ability_wc();
void program_end();


//Funções:
void program_title(){
    system ("title RuneScape Calculator");
}

void sys_lang(){
    setlocale(LC_ALL, "Portuguese");
}

void receive_nickname(){
    system("color 0B");
    printf("- Qual o seu nome? \n");
    printf("-> ");
    scanf("%s", &nickname);
    receive_ability_name();
}


void receive_ability_name(){
    printf("\n");
    printf("- Qual a habilidade que você deseja carregar? \n");
    printf("\n \t****************************\n");
    printf("\t* [1]\t- Corte de Lenha   *\n");
    printf("\t* [2]\t- Arte do Fogo     *\n");
    printf("\t****************************\n");
    printf("\n");
    printf("-> ");

    scanf("%i", &ability);
    switch(ability){
        case 1:
            system("cls");
            printf("Carregando código para Corte de Lenha... \n");
            sleep(3);
            system("cls");
            receive_ability_level();
            break;

        case 2:
            system("cls");
            printf("Carregando código para Arte do Fogo... \n");
            receive_ability_level();
            break;
    }
}


void receive_ability_level(){
    printf("\n");
    printf("- Então, %s, qual o seu nível nessa habilidade?\n", nickname);
    printf("-> ");
    scanf("%i", &ability_level);
    check_level();
}



void check_level(){
    if (ability_level < 1 || ability_level > 120){
        printf("O nível da habilidade deve ser entre 1 e 120.");
    }
    else{
        if (ability == 1){
             check_quantity_of_exp();
             ability_wc();
        }
        else if (ability == 2){
            printf("Faz o de FM!!!!");
        }


    }

}

void check_quantity_of_exp(){
    printf("\n");
    printf("- Qual quantidade de experiência necessária para atingir seu objetivo? \n");
    printf("-> ");
    scanf("%f", &xp_qnt);
}

void ability_wc(){
    printf("\n");
    printf("- Qual o tipo de árvore que você deseja cortar? \n");
    printf("-> ");
    scanf("%s", &log_cut_type);
    strcpy(type_normal, "normal");
    strcpy(type_oak, "carvalho");
    strcpy(type_willow, "salgueiro");
    strcpy(type_teak, "teca");
    strcpy(type_maple, "bordo");
    strcpy(type_mahogany, "mogno");
    strcpy(type_arctic_pine, "pinheiro do artico");
    strcpy(type_eucalyptus, "eucalipto");
    strcpy(type_yew, "teixo");
    strcpy(type_ivy, "hera");
    strcpy(type_magic, "magica");
    strcpy(type_blisterwood, "inflamadeira");
    strcpy(type_cursed_magic, "magica amaldiçoada");
    strcpy(type_mutated_vine, "vinha mutante");
    strcpy(type_curly_straight_root, "raiz curva");
    strcpy(type_ancient, "ancia");
    strcpy(type_crystal, "cristal");
    ret1 = strcmp(log_cut_type, type_normal);
    ret2 = strcmp(log_cut_type, type_oak);
    ret3 = strcmp(log_cut_type, type_willow);
    ret4 = strcmp(log_cut_type, type_teak);
    ret5 = strcmp(log_cut_type, type_maple);
    ret6 = strcmp(log_cut_type, type_mahogany);
    ret7 = strcmp(log_cut_type, type_arctic_pine);
    ret8 = strcmp(log_cut_type, type_eucalyptus);
    ret9 = strcmp(log_cut_type, type_yew);
    ret10 = strcmp(log_cut_type, type_ivy);
    ret11 = strcmp(log_cut_type, type_magic);
    ret12 = strcmp(log_cut_type, type_blisterwood);
    ret13 = strcmp(log_cut_type, type_cursed_magic);
    ret14 = strcmp(log_cut_type, type_mutated_vine);
    ret15 = strcmp(log_cut_type, type_curly_straight_root);
    ret16 = strcmp(log_cut_type, type_ancient);
    ret17 = strcmp(log_cut_type, type_crystal);

    if (ret1 == 0){
        if (ability_level >= 1){
                printf("Você receberá ao menos 25xp por lenha. \n");
                int xp_normal = 25;
                int price_for_sell = 94;
                float qtd_logs_needed = xp_qnt / xp_normal;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_normal){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }


    }
    else if (ret2 == 0){
        if (ability_level >= 15){
                printf("Você receberá ao menos 37.5xp por lenha. \n");
                int xp_oak = 37.5;
                int price_for_sell = 76;
                float qtd_logs_needed = xp_qnt / xp_oak;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_oak){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret3 == 0){
        if (ability_level >= 30){
                printf("Você receberá ao menos 67.5xp por lenha. \n");
                int xp_willow = 67.5;
                int price_for_sell = 22;
                float qtd_logs_needed = xp_qnt / xp_willow;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_willow){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret4 == 0){
        if (ability_level >= 35){
                printf("Você receberá ao menos 85xp por lenha. \n");
                int xp_teak = 85;
                int price_for_sell = 98;
                float qtd_logs_needed = xp_qnt / xp_teak;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_teak){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret5 == 0){
        if (ability_level >= 45){
                printf("Você receberá ao menos 100xp por lenha. \n");
                int xp_maple = 100;
                int price_for_sell = 25;
                float qtd_logs_needed = xp_qnt / xp_maple;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_maple){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret6 == 0){
        if (ability_level >= 50){
                printf("Você receberá ao menos 125xp por lenha. \n");
                int xp_mahogany = 125;
                int price_for_sell = 489;
                float qtd_logs_needed = xp_qnt / xp_mahogany;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_mahogany){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret7 == 0){
        if (ability_level >= 54){
                printf("Você receberá ao menos 140.2xp por lenha. \n");
                int xp_arctic_pine = 140.2;
                int price_for_sell = 71;
                float qtd_logs_needed = xp_qnt / xp_arctic_pine;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_arctic_pine){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret8 == 0){
        if (ability_level >= 58){
                printf("Você receberá ao menos 165xp por lenha. \n");
                int xp_eucalyptus = 165;
                int price_for_sell = 460;
                float qtd_logs_needed = xp_qnt / xp_eucalyptus;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_eucalyptus){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret9 == 0){
        if (ability_level >= 60){
                printf("Você receberá ao menos 175xp por lenha. \n");
                int xp_yew = 175;
                int price_for_sell = 169;
                float qtd_logs_needed = xp_qnt / xp_yew;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_yew){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret10 == 0){
        if (ability_level >= 68){
                printf("Você receberá ao menos 332.5xp por lenha. \n");
                int xp_ivy = 332.5;
                float qtd_logs_needed = xp_qnt / xp_ivy;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);

                if (xp_qnt == 1 || xp_qnt == xp_ivy){
                    qtd_logs_needed = 1;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }

    else if (ret11 == 0){
        if (ability_level >= 75){
                printf("Você receberá ao menos 250xp por lenha. \n");
                int xp_magic = 250;
                int price_for_sell = 613;
                float qtd_logs_needed = xp_qnt / xp_magic;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_magic){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret12 == 0){
        if (ability_level >= 76){
                printf("Você receberá ao menos 200xp por lenha. \n");
                int xp_blisterwood = 200;
                float qtd_logs_needed = xp_qnt / xp_blisterwood;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);

                if (xp_qnt == 1 || xp_qnt == xp_blisterwood){
                    qtd_logs_needed = 1;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret13 == 0){
        if (ability_level >= 82){
                printf("Você receberá ao menos 275xp por lenha. \n");
                int xp_cursed_magic = 275;
                int price_for_sell = 94;
                float qtd_logs_needed = xp_qnt / xp_cursed_magic;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_cursed_magic){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret14 == 0){
        if (ability_level >= 83){
                printf("Você receberá ao menos 140xp por lenha. \n");
                int xp_mutated_vine = 140;
                float qtd_logs_needed = xp_qnt / xp_mutated_vine;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);

                if (xp_qnt == 1 || xp_qnt == xp_mutated_vine){
                    qtd_logs_needed = 1;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret15 == 0){
        if (ability_level >= 83){
                printf("Você receberá ao menos 161.6xp por lenha. \n");
                int xp_curly_straight_root = 161.6;
                float qtd_logs_needed = xp_qnt / xp_curly_straight_root;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);

                if (xp_qnt == 1 || xp_qnt == xp_curly_straight_root){
                    qtd_logs_needed = 1;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret16 == 0){
        if (ability_level >= 90){
                printf("Você receberá ao menos 325xp por lenha. \n");
                int xp_ancient = 325;
                int price_for_sell = 4896;
                float qtd_logs_needed = xp_qnt / xp_ancient;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);
                int total_profit = qtd_logs_needed * price_for_sell;

                if (xp_qnt == 1 || xp_qnt == xp_ancient){
                    qtd_logs_needed = 1;
                    total_profit = price_for_sell;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                    total_profit = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
                printf("Lucro total: %i moeda(s). \n", total_profit);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }

    }
    else if (ret17 == 0){
        if (ability_level >= 94){
                printf("Você receberá ao menos 434.5xp por lenha. \n");
                int xp_crystal = 434.5;
                float qtd_logs_needed = xp_qnt / xp_crystal;
                int qtd_logs_needed_up = ceil(qtd_logs_needed);

                if (xp_qnt == 1 || xp_qnt == xp_crystal){
                    qtd_logs_needed = 1;
                }
                else if (xp_qnt == 0){
                    qtd_logs_needed = 0;
                }

                printf("%s, você precisará cortar aproximadamente %i árvore(s). \n", nickname, qtd_logs_needed_up);
        }
        else{
            printf("Você não possui o nível necessário para cortar este tipo de lenha.");
        }


    }
    else{
        printf("O tipo de lenha informado é inválido. Lembre-se de digitar sem acentos!\n");
    }

}

void program_end(){
    sleep(10);
    system("cls");
    printf("\t \t \t \t-> Fim do programa. <-");
    sleep(5);
}
