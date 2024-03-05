---
title: Comprobar el número de versión del componente
type: docs
weight: 70
url: /es/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

En algunos casos, es posible que se pregunte qué versión del producto tiene. A menudo creamos nuevas correcciones (correcciones de errores para los escenarios de los usuarios que señalan) y las publicamos en los foros en función de sus necesidades con urgencia. El número de versión consta del número de versión principal, el número de versión secundaria y el número de versión de revisión. Todos los componentes definidos deben ser números enteros mayores o iguales a 0. El formato del número de versión es el siguiente:

major.minor.hotfix, podemos aumentar una parte en 1 y hacer una nueva versión. Normalmente, aumentamos la última parte en 1 y creamos una nueva solución para publicarla en los foros para los usuarios.

Este documento describe algunas formas de verificar qué versión del componente está instalada en su sistema.

{{% /alert %}} 
## **Comprobación del número de versión**
### **1) Manera Manual**
Si tiene la versión/corrección Java (Aspose.Cells for Java), puede descomprimir el archivo jar de la biblioteca Aspose.Cells, abrir el archivo MANIFEST con el bloc de notas y buscar la cadena, es decir, "Specification-Version:" para verificar su valor.

![todo:imagen_alternativa_texto](check-version-number-of-the-component_1.png)


**Figura:** Comprobación del número de versión de la corrección Java
### **2) Uso de las API**
También puede usar las siguientes API para obtener el número de versión del producto.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

