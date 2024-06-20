---
title: No se encuentra sobrecarga para el método Guardar con 4 argumentos
type: docs
weight: 70
url: /es/net/no-overload-for-method-save-takes-4-arguments/
---

## **Síntoma**

"Al usar la versión de Aspose.Cells, obtengo este error cuando uso el método Guardar al intentar guardar el libro de trabajo en el objeto de Respuesta. Encuentro este fragmento de código documentado en la documentación en línea."

### **Captura de pantalla del error**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **Solución**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET es compatible y funciona bien con todas las versiones del framework .NET, es decir, 2.x, 3.x, 4.x, etc. para cualquier tipo de proyecto como Asp.NET/Winforms, proyecto web, Aplicación de consola u otros proyectos, etc. Proporcionamos diferentes dlls para las diferentes versiones del framework .NET. Para más información, lee el archivo **readme.txt** en la carpeta "\Bin" en tu directorio de instalación. Sin embargo, este archivo **readme.txt** está presente.

Cuando uses nuestro producto en una aplicación web, por favor utiliza el Aspose.Cells.dll de la carpeta **NET 2.0** en el directorio "/bin". Para tu información, el archivo dll en el directorio **.NET 3.5 Client Profile** se utiliza solo para la aplicación de consola con el perfil de cliente del framework Net como el framework objetivo de VS.NET. Por favor verifica tu proyecto, es posible que tu proyecto esté haciendo referencia a este archivo dll.

### **Referencias**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
