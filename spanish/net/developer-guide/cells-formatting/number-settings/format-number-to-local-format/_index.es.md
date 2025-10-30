---
title: Cómo formatear números al formato de idioma local
type: docs
weight: 10
url: /es/net/how-to-format-number-to-local-language-format/
description: Este artículo presentará cómo formatear números al formato de idioma local usando la API Aspose.Cells for .NET.
keywords: Convertir un número en un formato del idioma local, Transformar un dígito en su formato del idioma local, Cambiar un número a su formato correspondiente en el idioma local, Formatear un valor numérico en un formato del idioma local, Expresar un número en formato del idioma local, Formatear Número al formato del idioma local.
---

## **Escenarios de uso posibles**

Formatear números en Excel en formatos locales es esencial para garantizar que los datos sean claramente entendidos, interpretados con precisión y presentados de manera profesional en diferentes regiones y culturas.

1. **Adaptación Cultural y Regional**: Diferentes regiones utilizan varios formatos numéricos para decimales, separadores de miles, monedas y fechas. 
1. **Profesionalismo y Claridad**: Utilizar formatos locales mejora la apariencia profesional de tus hojas de cálculo. Demuestra atención al detalle y consideración por la audiencia, lo cual es crucial en informes, estados financieros y datos compartidos con partes interesadas.
1. **Consistencia en la Visualización de Datos**: El formateo local garantiza consistencia al colaborar con equipos o clientes de diferentes regiones. Previene errores que puedan surgir por la interpretación errónea de datos, como confundir los separadores decimales.
1. **Compatibilidad con Sistemas Externos**: Al exportar datos a otros formatos (por ejemplo, CSV), el formateo local ayuda a mantener la integridad de los datos.
1. **Accesibilidad y Facilidad de Uso**: El formateo local hace que los datos sean más accesibles para usuarios que no están familiarizados con formatos extranjeros. Por ejemplo, mostrar fechas en el formato "DD/MM/AAA" (común en el Reino Unido) frente a "MM/DD/AAA" (común en EE. UU.) evita confusiones.
1. **Validación y Precisión de Datos**: El formateo incorrecto puede llevar a errores en cálculos. Por ejemplo, si un número se interpreta mal debido a problemas con el separador decimal, las fórmulas pueden producir resultados incorrectos. Usar formatos locales asegura que los datos ingresados por los usuarios estén alineados con los estándares regionales, reduciendo el riesgo de errores durante la entrada o análisis de datos.

## **Cómo dar formato a un número en formato del idioma local en Excel**

Para dar formato a números en el idioma local en Excel, puedes usar varias funciones y características integradas que se adaptan a diferentes configuraciones regionales. 

1. **Usar la Configuración Regional Integrada en Excel**: Ve a Archivo > Opciones > Configuración Regional (o similar, según tu versión de Excel). Selecciona tu idioma/región deseada (ejemplo, Alemán para separadores decimales con coma, Inglés para puntos). Los valores y fórmulas existentes se convertirán automáticamente al nuevo formato.
1. **Usar la Función TEXTO para Formatos Localizados Personalizados**: La función TEXTO puede forzar el formato numérico según patrones específicos del locale, útil para mostrar números como números telefónicos o monedas sin alterar la configuración global. Sintaxis: =TEXTO(valor, "código_de_formato").
1. **Manejo Programático (VBA/APIs)**: Para desarrolladores que usan VBA, puedes usar NumberFormat con cadenas de formato en inglés de EE. UU. (por ejemplo, "#.##"). Excel se adaptará automáticamente a la configuración regional del usuario. Evita NumberFormatLocal a menos que necesites explícitamente cadenas de formato específicas del locale.
1. **Sobrescribir los Separadores del Sistema en Casos Específicos**: Si el formateo localizado se comporta de manera inesperada (por ejemplo, debido a actualizaciones de Windows que afectan los separadores), sobrescribe manualmente los valores predeterminados: en las opciones de Excel, desmarca "Usar separadores del sistema" y define tus propios separadores decimales y de miles.
1. **Formatear Número Usando un Formato Personalizado**: Haz clic derecho en la celda, selecciona 'Formato de celdas', luego 'Número' -> 'Personalizado' y establece el tipo de número personalizado deseado. Tomando como ejemplo el establecimiento de formatos numéricos personalizados en un entorno chino.
<br>
<img src="1.png" width=60% />


## **Cómo dar formato a un número en formato del idioma local en Aspose.Cells for .NET**

Para dar formato a números en el número Aspose.Cells for .NET en formato del idioma local, puedes usar el objeto `Style` asociado a una celda o rango de celdas. El objeto `Style` te permite establecer varias opciones de formato, incluyendo el formato numérico personalizado. 

Aquí tienes un ejemplo básico de cómo aplicar un formato numérico en el idioma local a una celda en Aspose.Cells for .NET:

1. **Referencia Aspose.Cells**: Asegúrese de tener referenciado Aspose.Cells for .NET en su proyecto. Puede obtenerlo desde NuGet o desde el sitio web de Aspose.

2. **Crear o Abrir un Libro de Trabajo**: Comienza creando un nuevo libro o abriendo uno existente.

3. **Acceder a la celda deseada**: Identifica y accede a la celda o rango de celdas que deseas formatear.

4. **Aplicar Formato Numérico Personalizado**: Establece el formato numérico de la celda a un formato en idioma chino.

4. **Código de ejemplo**: Aquí tienes un fragmento de código que demuestra estos pasos.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-FormatNumber-To-LocalLanguageFormat.cs" >}}

## **Salida generada por el código de ejemplo**
Aquí está el resultado en pdf del código de ejemplo anterior.
<br>
<img src="2.png" width=60% />

{{< app/cells/assistant language="csharp" >}}
