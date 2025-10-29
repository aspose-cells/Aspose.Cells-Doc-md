---
title: Configuration de la mise en page et des options d impression
type: docs
weight: 60
url: /fr/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. La mise en page et les paramètres d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells pour Python via .NET.

Cet article montre comment créer une application console dans Visual Studio.Net, et appliquer la mise en page et les options d'impression à une feuille de calcul avec quelques lignes de code simples en utilisant l'API Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Travailler avec la mise en page et les paramètres d'impression**

Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisé Aspose.Cells pour Python via .NET pour définir la mise en page et les options d'impression.

### **Utilisation d'Aspose.Cells pour définir les options de mise en page**

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez des options de mise en page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.

| **Fichier de sortie.** |
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Créez une feuille de calcul avec des données dans Microsoft Excel:
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Ajoutez des données.
1. Définir les options de mise en page :
   Appliquer les options de mise en page au fichier. Ci-dessous se trouve une capture d'écran des options par défaut, avant l'application des nouvelles options.

| **Options de mise en page par défaut.** |
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

### **Paramétrage des options d'impression**

Les paramètres de mise en page fournissent également plusieurs options d'impression (appelées également options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul. Ils permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique d'une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

L'exemple qui suit applique des options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application de nouvelles options.

|**Document d'entrée**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
L'exécution du code modifie les options d'impression.

|**Fichier de sortie**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
