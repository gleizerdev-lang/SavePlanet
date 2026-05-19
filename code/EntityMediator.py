from code.Const import WIN_HEIGHT, PLAYER_HIT_DAMAGE, PLANET_HIT_DAMAGE
from code.Enemy import Enemy
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.bottom < 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2, entity_list: list[Entity]):
        if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):

            if (isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot)) or \
                    (isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)):
                ent1.health -= getattr(ent2, 'damage', 10)
                ent2.health -= getattr(ent1, 'damage', 10)
                ent1.last_dmg = getattr(ent2, 'name', 'PlayerShot')
                ent2.last_dmg = getattr(ent1, 'name', 'Enemy')

            elif (isinstance(ent1, Enemy) and getattr(ent2, 'name', '') == 'Player') or \
                    (getattr(ent1, 'name', '') == 'Player' and isinstance(ent2, Enemy)):

                enemy = ent1 if isinstance(ent1, Enemy) else ent2
                player = ent2 if getattr(ent2, 'name', '') == 'Player' else ent1

                if not getattr(enemy, 'player_damage_applied', False):
                    player.health -= PLAYER_HIT_DAMAGE
                    player.last_dmg = getattr(enemy, 'name', 'Enemy')

                    enemy.health -= getattr(player, 'damage', 0)
                    enemy.last_dmg = getattr(player, 'name', 'Player')

                    setattr(enemy, 'player_damage_applied', True)

            elif (isinstance(ent1, Enemy) and getattr(ent2, 'name', '') == 'Planet') or \
                    (getattr(ent1, 'name', '') == 'Planet' and isinstance(ent2, Enemy)):

                enemy = ent1 if isinstance(ent1, Enemy) else ent2
                planet = ent2 if getattr(ent2, 'name', '') == 'Planet' else ent1

                limite_de_dano = planet.rect.top + (planet.rect.height * 0.2)

                if enemy.rect.bottom >= limite_de_dano and not getattr(enemy, 'planet_damage_applied', False):
                    for ent in entity_list:
                        if getattr(ent, 'name', '') == 'Player':
                            # O DANO DE INVASÃO DO PLANETA VAI PARA O JOGADOR
                            ent.health -= PLANET_HIT_DAMAGE
                            ent.last_dmg = getattr(enemy, 'name', 'Enemy')

                    setattr(enemy, 'planet_damage_applied', True)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if getattr(enemy, 'last_dmg', '') == 'PlayerShot':
            for ent in entity_list:
                if getattr(ent, 'name', '') == 'Player':
                    ent.score += getattr(enemy, 'score', 0)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2, entity_list)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list.copy():
            if getattr(ent, 'health', 1) <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)