==============================================
Infraestructura y sitio web para Python México
==============================================

En éste repositorio encontrarás el código fuente usado para construir
el sitio web de Python México. Si eres curioso podrás aprender cómo se
ha construido.

El plan es ofrecer la infraestructura necesaria para que la Comunidad
Python de México pueda crecer y desarrollarse. Es por eso que se
preparará el sitio para ofrecer tres diferentes servicios.

 * La página frontal y noticias con `Plone <http://plone.org>`_.

 * El wiki con `MoinMoin <http://moinmo.in/>`_.

 * Para tutoriales extensos y documentación estructurada, se usará
   `Sphinx <http://sphinx.pocoo.org/>`_ y `ReStructuredText
   <http://docutils.sourceforge.net/rst.html>`_.

 * Usaremos `Diazo <http://diazo.org/>`_ para darle una
   apariencia común a los 3 servicios.

 * Tras bambalinas: Buildout, paster, uwsgi, Python, nginx y/o Apache.

Estado actual
-------------

 * Plone 4.1 : Instalado y funcionando con uwsgi.
 
 * Diazo: Funcionando

 * MoinMoin: Integrado, gracias a `Erik Rivera <http://rivera.pro/>`_
   que escribió la `receta de buildout
   <https://github.com/PythonMexico/collective.recipe.moin>`_ para
   construir un sitio wsgi.

Instrucciones para desarrolladores
----------------------------------

Antes de empezar, si aún no tienes una cuenta en GitHub, pide una. Es
gratis. Si quieres aprender a usar Git, te recomendamos que te des una
vuelta por el sitio oficial: http://git-scm.com/documentation

El siguiente paso es instalar las librerías de desarrollo de
Python. En Debian y Ubuntu, puedes ejecutar::

    apt-get install build-essential python-dev libxslt1-dev git

Una vez que hayas instalado lo necesario, deberás clonar el repositorio::

    git clone git://github.com/PythonMexico/pythonmx_site.git

Ésto creará una carpeta con el nombre ``pythonmx_site``. Abre esa
carpeta y ejecuta el script ``bootstrap.py``::

    python bootstrap.py

Si todo sale bien, al final del proceso, se te informará que se creó
un script en ``bin/buildout``. Hay que ejecutarlo desde adentro de la
carpeta ``pythonmx_site``::

    bin/buildout

Ve por un café o té, por que el proceso tardar varios minutos
dependiendo de la velocidad de tu conexión a internet. Finalmente
buildout creará varios scripts en el directorio
``pythonmx_site/bin``. He aquí la lista de los más interesantes::

 * ``bin/plone fg`` arranca Plone en modo "foreground". Presiona
   <ctrl>+<C> para terminarlo.

 * ``bin/rundiazo`` arranca el servidor diazo (que es el que aplica
   estilos a Plone y MoinMoin.


