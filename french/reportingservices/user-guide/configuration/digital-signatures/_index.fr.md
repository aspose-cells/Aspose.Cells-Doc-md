---
title: Signatures numériques
type: docs
weight: 50
url: /fr/reportingservices/digital-signatures/
---
 Aspose.Cells pour Reporting Services prend en charge les signatures numériques lors de l'exportation de fichiers Microsoft Excel 2007 ou de fichiers ODS. Nous avons des informations de configuration pour les signatures numériques qui peuvent être définies dans le**Aspose.Cells.ReportingServices.xml** dossier.

 Lorsque la valeur de DigitalSignature est**à l'arrêt**, Aspose.Cells pour Reporting Services désactive les signatures numériques.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 Lorsque la valeur de DigitalSignature est**sur**, Aspose.Cells pour Reporting Services active les signatures numériques.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Il y a quatre paramètres dans la section DigitalSignature. Ceux-ci sont:

- **Nom**représente un rapport nécessitant une signature numérique. Lorsque le paramètre est laissé vide, les rapports utilisent un fichier PFX pour les signatures numériques.
- **pfxNomFichier**: fait référence à un fichier PFX. Le nom de fichier doit être un nom de fichier complet, avec chemin et extension de fichier. Ne doit pas être vide.
- **pfxPwd**: définit le mot de passe. Ne doit pas être vide.
- **objectif**: une description de l'objet de la signature. Peut être vide.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
