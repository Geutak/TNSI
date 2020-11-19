liste_caractère = ["Intelligent, doté d’une très bonne mémoire, il est compétent mais pas très minutieux dans son travail. Il a de grandes facilités à s’adapter dans un nouvel environnement. Il n’est pas très chanceux en amour.",
" Toujours occupé, le coq se plaît au travail. Il va toujours essayer de nouvelles choses quitte à être déçu. Aime bien les activités sociales et est un peu rêveur. ",
"Honnête, franc et tolérant, il regroupe tous les bons caractères de l’Homme. Se plaît dans les activités sociales. Il est têtu et délicat.",
" Très patient, il a beaucoup de projets. Pas beaucoup d’amis mais ils sont très importants pour lui. Il n’aime pas les disputes et n’a pas beaucoup de chance en amour.",
"Souriant et aimable, le rat est très sociable. Il s’inquiète et se fâche vite. Le rat a très confiance en lui et accorde beaucoup d’importance à son apparence. ",
" Timide et assidu, le buffle est très patient, pourtant il peut vite se fâcher. Pour lui, le travail est le plus important, plus que la famille.",
"sensible, le tigre aime séduire et plaire. Il est très indécis quand il y a des décisions à prendre. Le tigre est patient et un peu égoïste.",
"Il a beaucoup de succès dans le travail et gagne beaucoup d’argent pourtant il reste très modeste. La famille est très importante pour lui. Sociable, il a un grand réseau. Le chat est très chanceux.",
" Toujours en bonne santé, le dragon est très actif et a de grandes facilités à devenir riche. Têtu, tolérant, il est facilement influençable.",
"Très intelligent et chanceux, il arrive facilement à avoir du succès dans le travail mais il veut toujours se montrer, se mettre en avant et est demandeur de compliments. Égoïste et avare.",
"Très jovial, très bavard, il est sociable et aimable et doué dans le commerce. Sensible, exigeant, il est minutieux dans le travail. Ne s’intéresse pas trop à l’amour où il est très naïf et préfère une carrière professionnelle.",
" Très sensible, elle est enthousiaste au début mais vite déçue. Quelques fois pessimiste. Facilité à s’adapter avec les autres."]




while True:
    try:
        d = input('Entrez votre date de naissance au format jj/mm/aaaa')
        d=d.split("/")
        j=int(d[0])
        m=int(d[1])
        a=int(d[2])
        try:
            if m<1 or m>12:

                raise ValueError
        except ValueError:
            print("Ton mois doit être en chiffres et entre 1 et 12.")
            raise
        try:

            if m <=7:
                if m == 2:
                    if a % 4 == 0:
                        if a % 100 == 0:
                            if a % 400 != 0:

                               x = 29
                        x=29
                    else:
                        x = 28

                elif m % 2 == 0:
                    x = 30

                else:
                    x = 31
            else:
                if m % 2 == 0:
                    x = 31
                else:
                    x = 30
            if 1<= j <=x:
                break
            raise ValueError
        except ValueError:
            print("Ton jour doit être en chiffres et entre 1 et {}.".format(x))
            raise
    except ValueError:
        print("Ta date de naissance doit etre en chiffre au format jj/mm/aaaa  doit être en chiffres.")

    except IndexError:
        print("Vous avez oublié une partie de votre date de naissance.")
print("Vous êtes né le",j,"/",m,"/",a,".")
signe_vietnamien = ["singe","coq","chien","cochon","rat","buffle","tigre","chat","dragon","serpent","cheval","chèvre"]
r = a%12
print("Selon votre année de naissance, vous êtes ",signe_vietnamien[r],".","\n",liste_caractère[r])
