# Requisitos del sistema

## Requisitos funcionales

| ID | Requisito | Criterio de aceptación |
|----|-----------|------------------------|
| RF01 | El sistema permitirá registrar, editar y eliminar productos | Un producto nuevo aparece en el listado en menos de 2 segundos tras guardarse |
| RF02 | El sistema controlará las existencias de cada producto | Cada venta o compra actualiza el stock de forma inmediata y exacta |
| RF03 | El sistema alertará cuando un producto llegue a su stock mínimo | La alerta se muestra cuando las existencias son iguales o menores al mínimo definido |
| RF04 | El sistema permitirá registrar ventas | Una venta con 10 productos se registra en menos de 5 segundos |
| RF05 | El sistema generará un comprobante por cada venta | El comprobante muestra fecha, productos, cantidades y total correcto |
| RF06 | El sistema permitirá registrar compras a proveedores | La entrada de mercancía incrementa el stock del producto correspondiente |
| RF07 | El sistema generará reportes de ventas e inventario | El reporte se genera por rango de fechas y coincide con los registros |
| RF08 | El sistema gestionará usuarios con roles | Un cajero no puede acceder a las opciones de administración |

## Requisitos no funcionales

| ID | Requisito | Criterio de aceptación |
|----|-----------|------------------------|
| RNF01 | Usabilidad: interfaz sencilla para personal sin experiencia técnica | Un usuario nuevo registra una venta tras 15 minutos de capacitación |
| RNF02 | Rendimiento: respuesta ágil en operaciones frecuentes | 95 % de las consultas responden en menos de 3 segundos |
| RNF03 | Seguridad: acceso mediante usuario y contraseña | Las contraseñas se almacenan cifradas |
| RNF04 | Disponibilidad: operación durante el horario del negocio | Disponibilidad mínima del 98 % en horario comercial |
| RNF05 | Mantenibilidad: código y documentación organizados | Cada módulo se documenta en el repositorio |

## Interesados
Propietario del colmado, cajeros, proveedores, clientes, equipo de desarrollo.
