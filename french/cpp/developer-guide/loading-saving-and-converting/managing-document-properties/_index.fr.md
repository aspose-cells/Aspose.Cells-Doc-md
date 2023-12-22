---
title: Gestion des propriétés du document
type: docs
weight: 30
url: /fr/cpp/managing-document-properties/
---
##  **Scénario d'utilisation possible**
 Aspose.Cells vous permet de travailler avec les propriétés de document intégrées et personnalisées. Voici l'interface Excel Microsoft pour ouvrir ces derniers*Propriétés du document*. Cliquez simplement sur * Propriétés avancées*comme indiqué dans cette capture d'écran et visualisez-les.

![tâche : image_alt_text](managing-document-properties_1.png)
##  **Gestion des propriétés du document**
 L'exemple de code suivant se charge[exemple de fichier Excel](23166989.xlsx) et lit les propriétés du document intégré, par exemple*Titre, Sujet* puis les change. Ensuite, il lit également la propriété du document personnalisé, c'est-à-dire*MaPersonnalisée1* puis ajoute une nouvelle propriété de document personnalisée, c'est-à-dire*MaPersonnalisée5* et écrit le[sortie du fichier Excel](23166986.xlsx)La capture d'écran suivante montre l'effet de l'exemple de code sur l'exemple de fichier Excel.

![tâche : image_alt_text](managing-document-properties_2.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


##  **Sortie console**
 Il s'agit de la sortie console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le[exemple de fichier Excel](23166989.xlsx).

{{< highlight "java" >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
