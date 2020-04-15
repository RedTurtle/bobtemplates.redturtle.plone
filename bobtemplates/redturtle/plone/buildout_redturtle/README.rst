
================
Stradanove Plone
================


Questo è il buildout per la parte Plone di Stradanove.

Prerequisiti
============

Questo buildout per girare, ha bisogno delle seguenti librerie di sistema:

- Python 3.7 e virtualenv
- Node lts (servirà per la parte Volto e per pm2)
- pm2

Installazione componenti NodeJS
-------------------------------

Per prima cosa bisogna installare la versione **lts** di **NodeJS** (attualmente v12.x).
Non ci serve usare nvm perché non abbiamo bisogno di gestire diverse versioni di node sulla macchina,
quindi va bene (anzi **bisogna**) installarlo di sistema.

Fatto questo, bisogna installare il gestore di processi `pm2`__::

    > npm install -g pm2

__ https://pm2.keymetrics.io/

Questa azione lo installerà globalmente.


Plone
=====

La componente Plone è come al solito dentro la cartella `components/plone` e va installata come al solito.

Riavvio istanze di produzione
-----------------------------

Da dentro la cartella `components/plone`::

    > make restart

Verranno riavviate le istanze a 30 secondi di distanza

Varnish
=======

La componente Varnish è come al solito dentro la cartella `components/plone` e va installata come al solito.

PM2 - Gestore dei processi
==========================

Visto che per la parte Volto è meglio usare un gestore di processi "*js-oriented*", per avere tutto in un unico posto,
gestiamo anche la parte Plone con **pm2**.

La cosa bella di pm2 è che il demone che gestisce i processi, è uno unico, quindi se su un server ci sono più installazioni,
si può vedere lo stato delle applicazioni in un unico punto.

Ogni installazione ha la sua configurazione: il file **ecosystem.config.js** che c'è in questo repo è un esempio
(non deve per forza chiamarsi così, basta che finisca per *config.js)::

    ...
    {
      script: "./components/plone/bin/zeoserver",
      args: "fg",
      name: "stradanove-plone-zeoserver",
      cwd: "/opt/stradanove/stradanove.buildout",
      interpreter:
        "/opt/stradanove/stradanove.buildout/components/plone/bin/python",
    },
    ...

Non è nient'altro che una serie di "*app*" da istanziare.

Stato dei processi
------------------

Il demone viene lanciato in automatico allo startup del sever. In alternativa basta lanciare il comando::

    > pm2 status

E prima di mostrare lo stato, fa partire il demone.

il comando `status` mostra lo stato di tutti i processi dati in pasto a pm2.

Caricamento delle app da gestire
--------------------------------

Per caricare una configurazione su pm2, basta eseguire il comando::

    > pm2 start ecosystem.config.js

Questo comando dirà a pm2 quali servizi far partire e come. Se il file è corretto, i servizi appariranno nello status.

Gestione processi
-----------------

Basta lanciare il comando::

    > pm2 start|stop|restart [nome-del-processo]

Se non si passa il nome del processo, l'azione viene eseguita su tutti.

Script di init
--------------

pm2 permette di creare in automatico lo script di init. Basta eseguire due comandi::

    > pm2 startup

Questo comando genererà un ulteriore comando da lanciare come root, per creare lo script di init con tutta la configurazione del caso.

Infine, bisogna lanciare il comando::

    > pm2 save

Questo fa un dump della configurazione attuale di pm2 (quali processi deve far girare) e al reboot verrà letto questo file per
sapere quali processi far partire in automatico.

Il comando `pm2 save` va lanciato ogni volta che viene modificato un qualunque servizio associato a pm2 (aggiunto, rimosso, cambiati parametri).

Per maggiori dettagli: https://pm2.keymetrics.io/docs/usage/startup/

Log
---

Per avere un log in tempo reale::

    > pm2 log

Poi ci sono tutti i log dei vari servizi in file nella home dell'utente.
