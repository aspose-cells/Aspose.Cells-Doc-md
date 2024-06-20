---
title: Establecer Tipo de Cifrado Fuerte
type: docs
weight: 10
url: /es/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) te permite cifrar y proteger con contraseña las hojas de cálculo. Utiliza algoritmos proporcionados por un Proveedor de Servicios Criptográficos (CSP). Un CSP es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000". Este es un CSP con algunos problemas de seguridad conocidos. Las hojas de cálculo que se aseguran con el tipo de cifrado "débil (XOR)" o con el tipo de cifrado "Compatible con Office 97/2000" se pueden vulnerar fácilmente.

Para superar este problema, utiliza uno de los tipos de cifrado fuertes proporcionados por Microsoft Excel. Puedes cambiar el tipo de cifrado al CSP más fuerte disponible. Para un cifrado fuerte, se requiere una longitud mínima de clave de 128 bits, por ejemplo, 'Proveedor Criptográfico Fuerte de Microsoft'.

También puedes cifrar y proteger con contraseña archivos de Excel con un tipo de cifrado fuerte utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Aplicar cifrado con Microsoft Excel**

Para implementar el cifrado de archivos en Microsoft Excel (por ejemplo 2007):

1. Desde el menú **Herramientas**, selecciona **Opciones**.
1. Selecciona la pestaña **Seguridad**.
1. Ingresa un valor para el campo **Contraseña para abrir**.
1. Haz clic en **Avanzado**.
1. Elige el tipo de cifrado y confirma la contraseña.

   **Configuración de cifrado en Microsoft Excel**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Aplicar cifrado con Aspose.Cells**

El siguiente ejemplo de código aplica un cifrado fuerte a un archivo y establece una contraseña.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
