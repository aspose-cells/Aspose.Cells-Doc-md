﻿---
title: Obtenir des informations sur la feuille de calcul
type: docs
weight: 50
url: /fr/net/get-worksheet-information/
---
## **OpenXML Excel**
{{< highlight "csharp" >}}

 chaîne FilePath = @"..\..\..\..\Sample Files\" ;

string FileName = FilePath + "Obtenir les informations de la feuille de calcul.xlsx" ;

GetSheetInfo(NomFichier);

Console.ReadKey();

}

public static void GetSheetInfo(string fileName)

{

vide statique privé GetSheetInfo (chaîne fileName)

{