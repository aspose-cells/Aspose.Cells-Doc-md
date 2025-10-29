---
title: Gestion des propriétés de document
type: docs
weight: 30
url: /fr/cpp/managing-document-properties/
---

## **Scénario d'utilisation possible**
Aspose.Cells vous permet de travailler avec les propriétés de document intégrées et personnalisées. Voici l'interface Microsoft Excel pour ouvrir ces *propriétés de document*. Cliquez simplement sur *Propriétés avancées* comme indiqué dans cette capture d'écran et visualisez-les.

![todo:image_alt_text](managing-document-properties_1.png)
## **Gestion des propriétés du document**
Le code d'exemple suivant charge [un fichier Excel d'exemple](23166989.xlsx) et lit les propriétés de document intégrées telles que *Titre, Sujet* puis les modifie. Ensuite, il lit également la propriété de document personnalisée, c'est-à-dire *MyCustom1* puis ajoute une nouvelle propriété de document personnalisée, c'est-à-dire *MyCustom5* et écrit le [fichier Excel de sortie](23166986.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple.

![todo:image_alt_text](managing-document-properties_2.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **Sortie console**
Il s'agit de la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple fourni](23166989.xlsx).

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
