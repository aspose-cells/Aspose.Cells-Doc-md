﻿---
title: Convertir la feuille de calcul en CSV
type: docs
weight: 30
url: /fr/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Convertir la feuille de calcul en CSV**
Si les développeurs ont besoin d'enregistrer leurs fichiers dans un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant le**TypeFormatFichier**énumération) en appelant le**sauvegarder**méthode de**Cahier**objet.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Convertir la feuille de calcul en CSV**
Le code ci-dessous montre comment la feuille de calcul peut être convertie en CSV en utilisant Apache POI HSSF et XSSF API par rapport à Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Un processeur rudimentaire XLSX -> CSV calqué sur le

\* Exemple de programme POI XLS2CSVmra par Nick Burch du

\* package org.apache.poi.hssf.eventusermodel.examples.

\* Contrairement à la version HSSF, celle-ci ignore complètement

\* lignes manquantes.

\* <p/>

\* Les fiches techniques sont lues à l'aide d'un analyseur SAX pour conserver

\* empreinte mémoire relativement petite, donc cela devrait être

\* capable de lire d'énormes classeurs. La table des styles et

\* la table de chaînes partagées doit être conservée en mémoire. Le

\* la classe de table de styles de POI standard est utilisée, mais une

La classe \* (lecture seule) est utilisée pour la table de chaînes partagées

\* parce que le POI standard SharedStringsTable se développe très

\* rapidement avec le nombre de chaînes uniques.

\* <p/>

\* Merci à Eric Smith pour un correctif qui corrige un problème

\* déclenché par des cellules avec plusieurs éléments "t", ce qui est

\* comment Excel représente différents formats (par exemple, un mot

\* clair et un mot en gras).

\*

\* @auteur Chris Lott

*/

public class ApacheXLSX2CSV {