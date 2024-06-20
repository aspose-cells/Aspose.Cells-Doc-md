---
title: Licence
type: docs
weight: 50
url: /fr/cpp/licensing/
---

## **Limitations de la version d'évaluation**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Appliquer la licence en utilisant un objet Fichier ou Flux**
La licence peut être chargée depuis un fichier ou un objet flux. Aspose.Cells for C++ essaiera de trouver la licence dans les emplacements suivants :

1. Chemin explicite.
1. Le dossier contenant Aspose.Cells.dll.
1. Le dossier contenant l'assemblée qui a appelé Aspose.Cells.dll.
1. Le dossier contenant l'assemblée d'entrée (votre .exe).
1. Une ressource intégrée dans l'assemblée qui a appelé Aspose.Cells.dll.

La manière la plus simple de définir une licence est de mettre le fichier de licence dans le même dossier que le fichier Aspose.Cells.dll et de spécifier le nom du fichier, sans chemin, comme indiqué dans l'exemple ci-dessous.
### **Chargement d'une Licence depuis un Fichier**
La manière la plus simple d'appliquer une licence est de mettre le fichier de licence dans le même dossier que le fichier Aspose.Cells.dll et de spécifier juste le nom du fichier sans chemin.

{{% alert color="primary" %}} 

Lorsque vous appelez la méthode SetLicense, le nom de licence que vous passez doit être celui du fichier de licence. Par exemple, si vous changez le nom du fichier de licence en "Aspose.Cells.lic.xml", passez ce nom de fichier à la méthode Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Chargement d'une Licence depuis un Objet Flux**
L'exemple suivant montre comment charger une licence depuis un flux.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
