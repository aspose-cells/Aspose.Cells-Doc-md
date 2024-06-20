---
title: Signatures numériques
type: docs
weight: 50
url: /fr/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services prend en charge les signatures numériques lors de l'exportation de fichiers Microsoft Excel 2007 ou ODS. Nous disposons de quelques informations de configuration pour les signatures numériques qui peuvent être définies dans le fichier **Aspose.Cells.ReportingServices.xml**.

Lorsque la valeur de DigitalSignature est **off**, Aspose.Cells for Reporting Services désactive les signatures numériques.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

Lorsque la valeur de DigitalSignature est **on**, Aspose.Cells for Reporting Services active les signatures numériques.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Il y a quatre paramètres dans la section DigitalSignature. Ceux-ci sont : 

- **name**: représente un rapport qui a besoin d'une signature numérique. Lorsque le paramètre est laissé vide, les rapports utilisent un fichier PFX pour les signatures numériques.
- **pfxFilename**: fait référence à un fichier PFX. Le nom du fichier doit être un nom de fichier entièrement qualifié, complet avec le chemin et l'extension de fichier. Ne doit pas être vide.
- **pfxPwd**: définit le mot de passe. Ne doit pas être vide.
- **purpose**: une description de ce pour quoi la signature est utilisée. Peut être vide.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
