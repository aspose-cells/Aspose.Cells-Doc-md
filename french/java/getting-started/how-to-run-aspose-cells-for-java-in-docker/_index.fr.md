---
title: Comment exécuter Aspose.Cells for Java dans Docker
type: docs
description: "Exécutez Aspose.Cells for Java dans un conteneur Docker pour Linux."
weight: 139
url: /fr/java/how-to-run-aspose-cells-in-docker/
---

Les microservices, conjointement avec la conteneurisation, permettent de combiner facilement les technologies. Docker vous permet d'intégrer facilement la fonctionnalité Aspose.Cells dans votre application, quelle que soit la technologie utilisée dans votre pile de développement.

Si vous ciblez les microservices, ou si la technologie principale de votre pile n'est pas .NET, C++ ou Java, mais que vous avez besoin de la fonctionnalité Aspose.Cells, ou si vous utilisez déjà Docker dans votre pile, alors vous pourriez être intéressé par l'utilisation de Aspose.Cells for Java dans un conteneur Docker.

## Prérequis

- Docker doit être installé sur votre système. 

## Créer une application Java

Dans cet exemple, vous créez une application Java qui crée un fichier xlsx simple, le sauvegarde et le lit. L'application peut ensuite être construite et exécutée dans Docker.

### Création de l'application Java

Créez l'application Java dans Eclipse en utilisant le code suivant. Dans cet exemple, nous utilisons Aspose.Cells for Java pour créer une nouvelle feuille de calcul xlsx et définir son nom de feuille et ses valeurs de cellule, puis les lire et les afficher.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Transformer l'application Java en package jar

La figure suivante montre comment créer un package jar en utilisant le menu "Export" dans Eclipse.

**![Créer un Jar en utilisant Eclipse](MakeJar.png)**

Maintenant que nous avons écrit un programme Java en utilisant Aspose.Cells for Java, nous avons un package jar. Ensuite, nous allons créer un fichier dockerfile.

### Configuration d'un Dockerfile

La prochaine étape consiste à créer et configurer le Dockerfile.

1. Créez le fichier dockerfile et placez-le à côté du package jar. Gardez ce nom de fichier sans extension (par défaut).
2. Dans le fichier dockerfile, spécifiez :

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Construction et Exécution de l'Application dans Docker

Maintenant l'application peut être construite et exécutée dans Docker. Ouvrez votre invite de commande préférée, changez de répertoire vers le dossier contenant le dockerfile et exécutez la commande suivante :

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

Après avoir exécuté la commande ci-dessus, vous obtiendrez le résultat de la feuille de calcul XLSX et le résultat de la ligne de commande. À ce stade, un programme Java a été exécuté avec succès dans Linux Docker.
{{< app/cells/assistant language="java" >}}
