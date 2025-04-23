---
title: Comment formater un nombre en date avec C++
linktitle: Comment formater un nombre en date
type: docs
weight: 10
url: /fr/cpp/format-number-to-date/
description: Cet article expliquera comment formater un nombre en date en utilisant l API Aspose.Cells for C++.
keywords: formater un nombre en date, paramètres de la cellule, formater un nombre en date, paramètres de date, format de date.
---

## **Scénarios d'utilisation possibles**
Formater des nombres en dates dans Excel (ou tout autre logiciel de tableur) est important pour plusieurs raisons, notamment lorsque vous travaillez avec des données comprenant des informations temporelles ou de planification. Voici pourquoi le formatage des nombres en dates est avantageux :

1. **Interprétation appropriée des valeurs de date** : Dans Excel, les dates sont stockées sous forme de numéros sériels (par exemple, 1 représente le 1er janvier 1900, et 44210 représente le 6 septembre 2021). Si ces nombres ne sont pas formatés en tant que dates, les utilisateurs verront des nombres sans signification au lieu de dates reconnaissables. Les formater correctement permet à Excel de les afficher en tant que véritables dates (par exemple, 06/09/2021 au lieu de 44210).
2. **Simplifie les calculs liés au temps** : Excel peut réaliser de nombreux calculs utilisant des dates, tels que calculer le nombre de jours entre deux dates, ajouter ou soustraire des jours, ou déterminer le jour de la semaine. Si les nombres ne sont pas formatés en tant que dates, Excel ne pourra pas effectuer ces opérations efficacement. Par exemple, si vous souhaitez connaître le nombre de jours entre le 01/09/2023 et le 01/10/2023, Excel peut le calculer facilement si les nombres sont au format date.
3. **Assure la cohérence** : Lorsque toutes les valeurs liées aux dates sont correctement formatées, cela garantit que toutes les dates apparaissent dans un style uniforme et lisible. Cette cohérence est importante dans les rapports commerciaux, les plannings de projets et les bases de données où la cohérence des dates est cruciale. Les différentes régions utilisent différents formats de date (par exemple, MM/JJ/AAAA aux États-Unis contre JJ/MM/AAAA dans de nombreux autres pays), donc le formatage aide à assurer une interprétation correcte des dates.
4. **Améliore la lisibilité** : Les dates présentées dans un format standard (par exemple, 01/01/2024) sont plus faciles à lire que des nombres sériels bruts comme 45000. Un formatage correct des dates rend votre feuille de calcul plus conviviale et évite toute confusion. Ceci est particulièrement important dans des scénarios tels que la planification, les échéanciers, la gestion d’événements ou les données historiques.
5. **Aide au tri et au filtrage** : Lorsque les dates sont correctement formatées, Excel les reconnaît comme de véritables dates, ce qui facilite le tri ou le filtrage des données chronologiquement. Par exemple, vous pouvez trier une liste d’événements par date ou filtrer une plage de données pour n’afficher que les enregistrements compris entre deux dates spécifiques. Sans un formatage correct, le tri peut s’effectuer en fonction du nombre brut au lieu des dates réelles.
6. **Permet l’utilisation de fonctions de date** : Excel propose une gamme de fonctions de date puissantes, telles que : AUJOURDHUI(), DATEDIF(), WORKDAY(), ANNEE(), MOIS(), JOUR(). Ces fonctions nécessitent que les dates soient correctement formatées pour des calculs précis.
7. **Prend en charge la visualisation (graphes / chronologies)** : Les dates formatées correctement peuvent être utilisées pour créer des graphiques et des diagrammes où le temps est une étape clé. Par exemple, dans un graphique chronologique, Excel a besoin de dates dans un format reconnu pour tracer les événements avec précision dans le temps. Des numéros mal formats ou non formatés peuvent entraîner des graphiques qui n’ont pas de sens ou qui reflètent des informations incorrectes.
8. **Empêche la mauvaise interprétation** : Les nombres bruts peuvent être facilement mal interprétés. Par exemple, 44210 pourrait être lu comme une valeur numérique générale, mais lorsqu’il est formaté en date, il est clair qu’il représente le 6 septembre 2021. Un formatage correct des dates aide à éviter toute mauvaise compréhension des données.
9. **Facilite la saisie de données** : Lorsque les cellules sont formatées en tant que dates, les utilisateurs sont invités à entrer des données dans un format de date valide, ce qui empêche les erreurs de saisie et garantit que les valeurs de date sont correctement capturées.
10. **Important pour la planification et le suivi** : Dans toute situation impliquant la planification, le suivi ou les échéances (comme la gestion de projet, la prévision financière ou les rapports sensibles au temps), le formatage des nombres en dates est crucial pour la précision et la compréhension. Il permet une meilleure planification et exécution.

## **Comment formater un nombre en date dans Excel**
Pour formater un nombre en date dans Excel, suivez ces étapes :

### **Utilisation du ruban (onglet Accueil)**
1. Sélectionnez les cellules contenant les nombres que vous souhaitez formater en dates.
2. Allez dans l'onglet Accueil du ruban.
3. Dans le groupe Nombre, cliquez sur la flèche déroulante dans la boîte de format Numérique (qui peut afficher "Général" ou "Nombre" par défaut).
4. Choisissez Date courte ou Date longue dans le menu déroulant. Date courte : affiche la date dans un format concis, par exemple, JJ/MM/AAAA (format international) ou MM/JJ/AAAA (format américain). Date longue : affiche la date dans un format plus descriptif, par exemple, lundi 1 janvier 2024.
<br>
<img src="1.png" width=60% />

### **Utilisation de la boîte de dialogue Format de cellule**
1. Sélectionnez les cellules que vous souhaitez formater.
2. Faites un clic droit sur les cellules sélectionnées et choisissez Format de cellule, ou appuyez sur Ctrl + 1 (Windows) ou Cmd + 1 (Mac).
3. Dans la boîte de dialogue Format de cellule, allez à l’onglet Nombre.
4. Dans la liste à gauche, sélectionnez Date.
5. Choisissez le format de date souhaité dans la liste à droite (par exemple, JJ/MM/AAAA, MM/JJ/AAAA, ou formats personnalisés).
<br>
<img src="2.png" width=60% />
6. Cliquez sur OK pour appliquer le format de date.

## **Comment formater un nombre en date dans Aspose.Cells**

Pour formater des nombres en date dans la bibliothèque Aspose.Cells for C++ pour travailler avec des fichiers Excel, vous pouvez appliquer le format de date aux cellules de manière programmatique. Voici comment le faire en utilisant C++ avec Aspose.Cells :

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the date format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
    a1.PutValue(44210);

    // Create a style object to apply the date format
    Style a1Style = a1.GetStyle();

    // "14" represents a standard date format in Excel (MM/DD/YYYY)
    a1Style.SetNumber(14);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(44210);

    // Create a style object to apply the date format
    Style a2Style = a2.GetStyle();

    // Custom format for YYYY-MM-DD
    a2Style.SetCustom(u"YYYY-MM-DD");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"DateFormatted.xlsx");

    Aspose::Cells::Cleanup();
}
```
