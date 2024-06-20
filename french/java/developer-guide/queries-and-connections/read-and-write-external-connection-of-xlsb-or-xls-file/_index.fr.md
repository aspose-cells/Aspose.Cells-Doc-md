---
title: Lire et écrire la connexion externe du fichier XLSB ou XLS
type: docs
weight: 80
url: /fr/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells prend déjà en charge la lecture et l'écriture de la connexion externe du fichier XLSX mais maintenant, il prend également en charge cette fonctionnalité pour les fichiers XLSB et XLS. Cependant, le code est le même pour les deux types de formats.

## **Lire et écrire la connexion externe du fichier XLSB/XLS**

Le code d'exemple suivant charge le fichier XLSB d'exemple (XLS peut également être chargé) et lit sa première connexion externe qui est en fait une connexion de base de données Microsoft Access. Il modifie ensuite la propriété [**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name) et l'enregistre en tant que fichier XLSB de sortie. La capture d'écran montre l'effet du code sur le [fichier XLSB d'exemple](51740743.xlsb) et le [fichier XLSB de sortie](51740742.xlsb) après son exécution. Veuillez également consulter la sortie de la console du code d'exemple ci-dessous pour référence.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Code d'exemple**

Le code suivant fonctionnera pour les fichiers XLSB et XLS en chargeant et en enregistrant les fichiers avec l'extension appropriée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Sortie console**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
