<!-- # Proposer un contenu

Merci de contribuer à enrichir ce site ! Ce formulaire vous permet de suggérer un ajout ou une modification de contenu.

<form action="https://formsubmit.co/critiquewiki@gmail.com" method="POST" style="max-width: 600px; margin-top: 2em;">

<div class="md-typeset__table">

<div style="display: flex; flex-direction: column; gap: 1em;">

  <label>
    <strong>Type de proposition</strong><br>
    <select name="action" required>
      <option value="ajout">Ajout</option>
      <option value="modification">Modification</option>
    </select>
  </label>

  <label>
    <strong>Type de contenu</strong><br>
    <select name="type" required>
      <option value="contre-argument">Contre-argument</option>
      <option value="notion">Notion</option>
      <option value="personnalité">Personnalité</option>
    </select>
  </label>

  <label>
    <strong>Contenu proposé</strong><br>
    <textarea name="contenu" rows="6" required placeholder="De la liste succinte à la page complète, tout est bienvenu :)"></textarea>
  </label>

  <label>
    <strong>Votre email (optionnel)</strong><br>
    <input type="email" name="contact" placeholder="email@example.com">
  </label>


  <input type="hidden" name="_next" value="/merci/">

  <input type="text" name="_honey" style="display:none">
  <input type="hidden" name="_captcha" value="false">

  <button type="submit" class="md-button">
    Envoyer la suggestion
  </button>

</div>
</div>

</form> -->

<!-- ---- -->

<form action="https://formsubmit.co/critiquewiki@gmail.com" method="POST" style="max-width: 600px; margin-top: 2em; display:flex; flex-direction:column; gap:1em;">

  <label for="action">Type de proposition</label>
  <select name="action" id="action" required>
    <option value="ajout">Ajout</option>
    <option value="modification">Modification</option>
  </select>

  <label for="type">Type de contenu</label>
  <select name="type" id="type" required>
    <option value="contre-argument">Contre-argument</option>
    <option value="évènement">Évènement</option>
    <option value="courant">Courant de pensée</option>
    <option value="notion">Notion</option>
    <option value="autre">Autre</option>
  </select>

  <label for="contenu">Contenu proposé</label>
  <textarea name="contenu" id="contenu" rows="6" required placeholder="De la liste succincte à la page complète, tout est bienvenu :)"></textarea>

  <label for="contact">Votre email (optionnel)</label>
  <input type="email" name="contact" id="contact" placeholder="email@example.com">

  <input type="hidden" name="_next" value="https://wikicritique.github.io/merci">
  <input type="text" name="_honey" style="display:none">
  <input type="hidden" name="_captcha" value="false">

  <button type="submit" class="md-button md-button--primary">Envoyer la suggestion</button>
</form>