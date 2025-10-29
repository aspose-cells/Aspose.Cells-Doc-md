---
title: Enregistrer le fichier dans l objet de réponse avec Golang via C++
linktitle: Enregistrement du fichier dans l objet de réponse
type: docs
weight: 50
url: /fr/go-cpp/saving-file-to-response-object/
description: Apprenez comment enregistrer des fichiers dynamiquement et les envoyer directement au navigateur d un client en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells permet de manipuler des fichiers. Cet article explique les différentes façons de sauvegarder des fichiers dans un objet de réponse.

{{% /alert %}}

## **Enregistrer le fichier dans l'objet Response**

Il est également possible de générer un fichier dynamiquement et de l'envoyer directement vers un navigateur client. Pour ce faire, utilisez une version surchargée spéciale de la méthode [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) qui accepte les paramètres suivants:

- Objet **HttpResponse**.
- Nom du fichier.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), le type de disposition de contenu du fichier de sortie.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), le type de format de fichier.

L'énumération [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) détermine si le fichier envoyé au navigateur fournit l'option de s'ouvrir directement dans le navigateur ou dans une application associée à .xls/.xlsx ou une autre extension.

L'énumération contient les types de sauvegarde prédéfinis suivants :

|**Type**|**Description**|
| :- | :- |
|Pièce jointe|Envoie la feuille de calcul au navigateur et l'ouvre dans une application en tant que pièce jointe associée à .xls/.xlsx ou autres extensions.|
|Incorporée|Envoie le document au navigateur et offre la possibilité de sauvegarder la feuille de calcul sur le disque ou l'ouvrir dans le navigateur.|

### **Fichiers XLS**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **Fichiers XLSX**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **Fichiers PDF**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Remarque**

En raison de l'objet "System.Web.HttpResponse" qui n'est pas inclus dans .NET5 et .Netstandard,
Cette fonction n'existe donc pas dans la version Aspose.Cells .NET5 et .Netstandard, vous pouvez vous référer au code suivant pour sauvegarder le fichier dans le flux, puis effectuer l'opération sur le flux.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
