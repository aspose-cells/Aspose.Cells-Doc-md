---
title: Gestion des propriétés de document
type: docs
weight: 30
url: /fr/go-cpp/managing-document-properties/
---

## **Scénario d'utilisation possible**

Aspose.Cells vous permet de travailler avec les propriétés de document intégrées et personnalisées. Voici l'interface Microsoft Excel pour ouvrir ces *propriétés de document*. Cliquez simplement sur *Propriétés avancées* comme indiqué dans cette capture d'écran et visualisez-les.

![todo:image_alt_text](managing-document-properties_1.png)

## **Gestion des propriétés du document**

Le code d'exemple suivant charge [fichier Excel d'exemple](23166989.xlsx) et lit les propriétés de document intégrées, par ex., *Titre et Sujet*, puis les modifie. Ensuite, il lit également la propriété personnalisée du document, c’est-à-dire, *MyCustom1*, et ajoute une nouvelle propriété personnalisée, c’est-à-dire, *MyCustom5*, puis écrit le [fichier Excel de sortie](23166986.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple.

![todo:image_alt_text](managing-document-properties_2.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](23166989.xlsx) fourni.

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}
