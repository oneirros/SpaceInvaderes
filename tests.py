import unittest

import ship
import constants
import collisions
import bullet
import levels


class SpaceInvadersTest(unittest.TestCase):

    def setUp(self):
        """Obiekty konieczne w testach."""
        self.player = ship.Player(
            constants.PLAYER_START_PLACE,
            constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT,
            constants.PLAYER_IMG,
            constants.PLAYER_HEALTH
        )

        self.alien = ship.Alien(
                    [320, 300],
                    30,
                    30,
                    constants.GREEN_ALIEN_IMG,
                    1
        )

        self.alien.shooting([320, 300], 5, False)

        self.player.shooting([self.player.position[0] + 3, self.player.position[1]], 1, True)


    def test_create_player(self):
        """Test konstruktora dla klasy Player"""
        self.assertIsInstance(self.player, ship.Ship)
        self.assertEqual(self.player.position, constants.PLAYER_START_PLACE)
        self.assertEqual(self.player.width, constants.PLAYER_WIDTH)
        self.assertEqual(self.player.height, constants.PLAYER_HEIGHT)
        self.assertEqual(self.player.img, constants.PLAYER_IMG)
        self.assertEqual(self.player.health, constants.PLAYER_HEALTH)

    def test_create_alien(self):
        """Test konstruktora dla klasy Alien"""
        self.assertIsInstance(self.alien, ship.Ship)
        self.assertEqual(self.alien.position, [320, 300])
        self.assertEqual(self.alien.width, 30)
        self.assertEqual(self.alien.height, 30)
        self.assertEqual(self.alien.img, constants.GREEN_ALIEN_IMG)
        self.assertEqual(self.alien.health, 1)

    def test_create_bullet(self):
        self.assertIsInstance(self.player.bullets[0], bullet.Bullet)
        self.assertEqual(self.player.bullets[0].position, [self.player.position[0] + 3, self.player.position[1]])
        self.assertEqual(self.player.bullets[0].speed, 1)
        self.assertEqual(self.player.bullets[0].direction, True)

    def test_player_alien_collision(self):
        """Test kolizji obiektów player i alien"""
        self.assertFalse(collisions.collide(self.player, self.alien))

        for i in range(100):
            self.alien.control()

        self.assertTrue(collisions.collide(self.player, self.alien))

    def test_player_bullet_collision(self):
        """Test kolizji obiektów player i bullet"""
        self.alien.shooting([320, 300], 5, False)
        self.assertFalse(collisions.collide(self.alien.bullets[0], self.player))

        for i in range(25):
            self.alien.bullets[0].movement()

        self.assertTrue(collisions.collide(self.alien.bullets[0], self.player))

    def test_alien_bullet_collizion(self):
        """Test kolizji obiektów alien i bullet"""
        self.alien.position = [320, 300]

        self.assertEqual(self.alien.position, [320, 300])
        self.assertEqual(self.player.bullets[0].position, [323, 400])
        self.assertFalse(collisions.collide(self.player.bullets[0], self.alien))

        for i in range(100):
            self.player.bullets[0].movement()

        self.assertTrue(collisions.collide(self.player.bullets[0], self.alien))

    def test_alien_out_off_screen(self):
        """Test funkcji wykrywającej obiekty poza oknem gry"""
        self.assertFalse(self.alien.out_off_screen())

        for i in range(600):
            self.alien.control()

        self.assertTrue(self.alien.out_off_screen())

    def test_bullet_out_off_screen(self):
        """Test funkcji wykrywającej obiekty poza oknem gry"""
        self.assertFalse(self.player.bullets[0].out_of_screen())

        for i in range(900):
            self.player.bullets[0].movement()

        self.assertTrue(self.player.bullets[0].out_of_screen())

    def test_which_level(self):
        """Test funkcji zwracający czas po jakim należy utworzyć nowego przeciwnika"""
        self.assertEqual(levels.tps_max_green_alien(49), 5.0)
        self.assertEqual(levels.tps_max_green_alien(99), 4.0)
        self.assertEqual(levels.tps_max_green_alien(250), 3.0)
        self.assertEqual(levels.tps_max_green_alien(768), 2.5)
        self.assertEqual(levels.tps_max_green_alien(1457), 2.0)
        self.assertEqual(levels.tps_max_green_alien(4893), 1.5)
        self.assertEqual(levels.tps_max_green_alien(7234), 1.0)
        self.assertEqual(levels.tps_max_green_alien(17234), 0.5)

        self.assertEqual(levels.tps_max_red_alien(700), 3.0)
        self.assertEqual(levels.tps_max_red_alien(1001), 2.5)
        self.assertEqual(levels.tps_max_red_alien(3456), 2.0)
        self.assertEqual(levels.tps_max_red_alien(5500), 2.0)
        self.assertEqual(levels.tps_max_red_alien(110001), 1.5)



if __name__ == "__main__":
    unittest.main()